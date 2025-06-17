"""
Tests for Doxygen MCP Server

Basic test suite to verify core functionality of the Doxygen MCP server.
"""

import asyncio
import json
import tempfile
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from server import DoxygenConfig, DoxygenServer


class TestDoxygenConfig:
    """Test the DoxygenConfig model"""
    
    def test_default_config(self):
        """Test default configuration values"""
        config = DoxygenConfig()
        assert config.project_name == "My Project"
        assert config.extract_all == True
        assert config.generate_html == True
        assert config.recursive == True
    
    def test_config_serialization(self):
        """Test Doxyfile generation"""
        config = DoxygenConfig(
            project_name="Test Project",
            output_directory="./test_docs",
            file_patterns=["*.cpp", "*.h"]
        )
        
        doxyfile_content = config.to_doxyfile()
        
        assert 'PROJECT_NAME           = "Test Project"' in doxyfile_content
        assert 'OUTPUT_DIRECTORY       = "./test_docs"' in doxyfile_content
        assert 'FILE_PATTERNS          = *.cpp *.h' in doxyfile_content
        assert 'EXTRACT_ALL            = YES' in doxyfile_content
    
    def test_language_optimization(self):
        """Test language-specific optimizations"""
        config = DoxygenConfig()
        config.optimize_output_for_c = True
        config.optimize_output_java = False
        
        doxyfile_content = config.to_doxyfile()
        
        assert 'OPTIMIZE_OUTPUT_FOR_C  = YES' in doxyfile_content
        assert 'OPTIMIZE_OUTPUT_JAVA   = NO' in doxyfile_content


class TestDoxygenServer:
    """Test the DoxygenServer implementation"""
    
    def setup_method(self):
        """Set up test environment"""
        self.server = DoxygenServer()
    
    @pytest.mark.asyncio
    async def test_list_tools(self):
        """Test tool listing functionality"""
        # Mock the server's list_tools handler
        tools = await self.server.server._tool_handlers["list_tools"]()
        
        assert len(tools) > 0
        
        # Check for key tools
        tool_names = [tool.name for tool in tools]
        assert "create_doxygen_project" in tool_names
        assert "generate_documentation" in tool_names
        assert "scan_project" in tool_names
        assert "check_doxygen_install" in tool_names
    
    @pytest.mark.asyncio
    async def test_create_project_success(self):
        """Test successful project creation"""
        with tempfile.TemporaryDirectory() as temp_dir:
            args = {
                "project_name": "Test Project",
                "project_path": temp_dir,
                "language": "cpp",
                "include_subdirs": True,
                "extract_private": False
            }
            
            result = await self.server._create_project(args)
            
            assert len(result) == 1
            assert "✅ Doxygen project 'Test Project' created successfully!" in result[0].text
            
            # Check if Doxyfile was created
            doxyfile_path = Path(temp_dir) / "Doxyfile"
            assert doxyfile_path.exists()
            
            # Verify content
            with open(doxyfile_path, 'r') as f:
                content = f.read()
            
            assert 'PROJECT_NAME           = "Test Project"' in content
            assert '*.cpp *.hpp *.cc *.hh *.cxx *.hxx' in content
    
    @pytest.mark.asyncio
    async def test_create_project_invalid_path(self):
        """Test project creation with invalid path"""
        args = {
            "project_name": "Test Project",
            "project_path": "/invalid/path/that/cannot/be/created",
            "language": "cpp"
        }
        
        result = await self.server._create_project(args)
        
        assert len(result) == 1
        assert "❌ Failed to create project:" in result[0].text
    
    @pytest.mark.asyncio
    async def test_scan_project_nonexistent(self):
        """Test scanning a non-existent project"""
        args = {
            "project_path": "/nonexistent/path"
        }
        
        result = await self.server._scan_project(args)
        
        assert len(result) == 1
        assert "❌ Project path does not exist:" in result[0].text
    
    @pytest.mark.asyncio
    async def test_scan_project_success(self):
        """Test successful project scanning"""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create some test files
            test_files = [
                "main.cpp",
                "header.h", 
                "utils.py",
                "config.json",
                "README.md"
            ]
            
            for filename in test_files:
                file_path = Path(temp_dir) / filename
                file_path.write_text(f"// Test content for {filename}")
            
            args = {
                "project_path": temp_dir
            }
            
            result = await self.server._scan_project(args)
            
            assert len(result) == 1
            result_text = result[0].text
            
            assert "📁 Project Scan Results" in result_text
            assert "Total Files Found: 5" in result_text
            assert ".cpp: 1 files" in result_text
            assert ".h: 1 files" in result_text
            assert ".py: 1 files" in result_text
    
    @pytest.mark.asyncio
    @patch('subprocess.run')
    async def test_check_doxygen_install_success(self, mock_run):
        """Test successful Doxygen installation check"""
        mock_run.return_value = MagicMock(
            returncode=0,
            stdout="1.9.4\n"
        )
        
        result = await self.server._check_doxygen_install({})
        
        assert len(result) == 1
        assert "✅ Doxygen 1.9.4 is installed and working!" in result[0].text
    
    @pytest.mark.asyncio
    @patch('subprocess.run')
    async def test_check_doxygen_install_not_found(self, mock_run):
        """Test Doxygen not found"""
        mock_run.side_effect = FileNotFoundError()
        
        result = await self.server._check_doxygen_install({})
        
        assert len(result) == 1
        assert "❌ Doxygen is not installed" in result[0].text
    
    @pytest.mark.asyncio
    async def test_generate_documentation_no_doxyfile(self):
        """Test documentation generation without Doxyfile"""
        with tempfile.TemporaryDirectory() as temp_dir:
            args = {
                "project_path": temp_dir,
                "output_format": "html"
            }
            
            result = await self.server._generate_documentation(args)
            
            assert len(result) == 1
            assert "❌ No Doxyfile found" in result[0].text
    
    @pytest.mark.asyncio
    @patch('subprocess.run')
    async def test_generate_documentation_success(self, mock_run):
        """Test successful documentation generation"""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create a mock Doxyfile
            doxyfile_path = Path(temp_dir) / "Doxyfile"
            doxyfile_path.write_text("PROJECT_NAME = Test")
            
            # Mock successful doxygen execution
            mock_run.side_effect = [
                MagicMock(returncode=0, stdout="1.9.4\n"),  # version check
                MagicMock(returncode=0, stderr="")  # documentation generation
            ]
            
            args = {
                "project_path": temp_dir,
                "output_format": "html"
            }
            
            result = await self.server._generate_documentation(args)
            
            assert len(result) == 1
            assert "✅ Documentation generated successfully!" in result[0].text


class TestLanguageDetection:
    """Test language-specific configuration"""
    
    def test_cpp_language_config(self):
        """Test C++ language configuration"""
        config = DoxygenConfig()
        
        # Simulate C++ project setup
        config.file_patterns = ["*.cpp", "*.hpp", "*.cc", "*.hh", "*.cxx", "*.hxx"]
        config.optimize_output_for_c = False
        
        doxyfile_content = config.to_doxyfile()
        
        assert "*.cpp *.hpp *.cc *.hh *.cxx *.hxx" in doxyfile_content
        assert "OPTIMIZE_OUTPUT_FOR_C  = NO" in doxyfile_content
    
    def test_python_language_config(self):
        """Test Python language configuration"""
        config = DoxygenConfig()
        
        # Simulate Python project setup
        config.file_patterns = ["*.py"]
        config.optimize_output_java = True  # Python uses Java-style optimization
        
        doxyfile_content = config.to_doxyfile()
        
        assert "FILE_PATTERNS          = *.py" in doxyfile_content
        assert "OPTIMIZE_OUTPUT_JAVA   = YES" in doxyfile_content
    
    def test_c_language_config(self):
        """Test C language configuration"""
        config = DoxygenConfig()
        
        # Simulate C project setup
        config.file_patterns = ["*.c", "*.h"]
        config.optimize_output_for_c = True
        
        doxyfile_content = config.to_doxyfile()
        
        assert "FILE_PATTERNS          = *.c *.h" in doxyfile_content
        assert "OPTIMIZE_OUTPUT_FOR_C  = YES" in doxyfile_content


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
