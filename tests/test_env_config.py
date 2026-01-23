
import os
import sys
import tempfile
import asyncio
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock

# Add src to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/src")

from doxygen_mcp.server import (
    create_doxygen_project,
    generate_documentation,
    query_project_reference,
    _resolve_project_path
)

@pytest.fixture
def temp_project_dir():
    with tempfile.TemporaryDirectory() as temp_dir:
        yield temp_dir

class TestEnvConfig:
    
    def test_resolve_project_path_explicit(self, temp_project_dir):
        """Test resolving path when explicitly provided"""
        resolved = _resolve_project_path(temp_project_dir)
        assert resolved == Path(temp_project_dir).resolve()

    def test_resolve_project_path_env(self, temp_project_dir):
        """Test resolving path from environment variable"""
        with patch.dict(os.environ, {"DOXYGEN_PROJECT_ROOT": temp_project_dir}):
            resolved = _resolve_project_path(None)
            assert resolved == Path(temp_project_dir).resolve()

    def test_resolve_project_path_missing(self):
        """Test error when path is missing entirely"""
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(ValueError):
                _resolve_project_path(None)

    @pytest.mark.asyncio
    async def test_create_project_with_env(self, temp_project_dir):
        """Test creating project using environment variable for path"""
        with patch.dict(os.environ, {"DOXYGEN_PROJECT_ROOT": temp_project_dir}):
            result = await create_doxygen_project(
                project_name="Env Project",
                # project_path is None by default
                language="python"
            )
            
            assert "✅ Doxygen project 'Env Project' created successfully!" in result
            assert (Path(temp_project_dir) / "Doxyfile").exists()

    @pytest.mark.asyncio
    async def test_generate_docs_with_env(self, temp_project_dir):
        """Test generating docs using environment variable"""
        # Create Doxyfile first
        (Path(temp_project_dir) / "Doxyfile").write_text("PROJECT_NAME=Test")
        
        with patch.dict(os.environ, {"DOXYGEN_PROJECT_ROOT": temp_project_dir}):
            with patch('subprocess.run') as mock_run:
                mock_run.side_effect = [
                    MagicMock(returncode=0, stdout="1.9.4\n"),  # version check
                    MagicMock(returncode=0, stderr="")  # generation
                ]
                
                result = await generate_documentation(
                    # project_path is None
                )
                
                assert "✅ Documentation generated successfully!" in result

    @pytest.mark.asyncio
    async def test_query_reference_with_env_xml(self, temp_project_dir):
        """Test querying with DOXYGEN_XML_DIR"""
        xml_dir = Path(temp_project_dir) / "xml"
        xml_dir.mkdir(parents=True)
        (xml_dir / "index.xml").write_text("<doxygenindex></doxygenindex>")
        
        with patch.dict(os.environ, {"DOXYGEN_XML_DIR": str(xml_dir)}):
             # Mock query engine to avoid actual parsing logic dependencies if possible,
             # or just ensure it returns something we can assert on (even error is fine if path found)
             
             with patch('doxygen_mcp.server.DoxygenQueryEngine') as mock_engine_cls:
                 mock_engine = mock_engine_cls.return_value
                 mock_engine.query_symbol.return_value = {"kind": "class", "name": "Test", "brief": "Brief", "detailed": "", "members": []}
                 
                 result = await query_project_reference("Test")
                 
                 assert "Documentation for class Test" in result
                 mock_engine_cls.assert_called_with(str(xml_dir))

    @pytest.mark.asyncio
    async def test_query_reference_with_project_root_env(self, temp_project_dir):
        """Test querying with DOXYGEN_PROJECT_ROOT implying XML location"""
        # Setup standard structure: root/docs/xml
        xml_dir = Path(temp_project_dir) / "docs" / "xml"
        xml_dir.mkdir(parents=True)
        (xml_dir / "index.xml").write_text("<doxygenindex></doxygenindex>")
        
        with patch.dict(os.environ, {"DOXYGEN_PROJECT_ROOT": temp_project_dir}):
             # Clear XML_DIR to ensure we use PROJECT_ROOT
             if "DOXYGEN_XML_DIR" in os.environ:
                 del os.environ["DOXYGEN_XML_DIR"]
                 
             with patch('doxygen_mcp.server.DoxygenQueryEngine') as mock_engine_cls:
                 mock_engine = mock_engine_cls.return_value
                 mock_engine.query_symbol.return_value = {"kind": "class", "name": "Test", "brief": "Brief", "detailed": "", "members": []}
                 
                 result = await query_project_reference("Test")
                 
                 assert "Documentation for class Test" in result
                 mock_engine_cls.assert_called_with(str(xml_dir))
