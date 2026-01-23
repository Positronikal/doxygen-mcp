#!/usr/bin/env python3
"""
Doxygen MCP Server - Context Aware Version
"""

import logging
import os
import subprocess
import json
from pathlib import Path
from typing import Optional, Dict, Any, List

# MCP server imports
from mcp.server.fastmcp import FastMCP
from .query_engine import DoxygenQueryEngine
from .config import DoxygenConfig
from .utils import resolve_project_path, detect_primary_language, get_ide_environment, update_ignore_file

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("doxygen-mcp")

mcp = FastMCP("Doxygen")

@mcp.tool()
async def get_context_info() -> Dict[str, Any]:
    """
    Get information about the current project context, detected language, and IDE environment.
    """
    project_path = resolve_project_path()
    language = detect_primary_language(project_path)
    ide_info = get_ide_environment()

    has_doxyfile = (project_path / "Doxyfile").exists()

    return {
        "project_root": str(project_path),
        "detected_language": language,
        "ide_environment": ide_info,
        "doxygen_status": {
            "has_doxyfile": has_doxyfile,
            "config_path": str(project_path / "Doxyfile") if has_doxyfile else None
        }
    }

@mcp.tool()
async def auto_configure(project_name: Optional[str] = None) -> str:
    """
    Automatically detect project settings and create a Doxyfile if one doesn't exist.
    """
    project_path = resolve_project_path()
    if not project_name:
        project_name = project_path.name

    language = detect_primary_language(project_path)

    if (project_path / "Doxyfile").exists():
        return f"✨ Project already configured at {project_path}. Detected language: {language}."

    result = await create_doxygen_project(
        project_name=project_name,
        project_path=str(project_path),
        language=language
    )

    return f"🚀 Auto-configured project!\n\n{result}"

@mcp.tool()
async def create_doxygen_project(
    project_name: str,
    project_path: Optional[str] = None,
    language: Optional[str] = None,
    include_subdirs: bool = True,
    extract_private: bool = False,
) -> str:
    """Initialize a new Doxygen documentation project with configuration"""
    try:
        # Resolve project path and detect language if not provided
        safe_project_path = resolve_project_path(project_path)
        if language is None:
            language = detect_primary_language(safe_project_path)

        if safe_project_path.exists() and not safe_project_path.is_dir():
            return f"❌ Path exists but is not a directory: {safe_project_path}"

        # Create project directory if it doesn't exist
        safe_project_path.mkdir(parents=True, exist_ok=True)

        # Create configuration based on language
        config = DoxygenConfig(
            project_name=project_name,
            output_directory=str(safe_project_path / "docs"),
            input_paths=[str(safe_project_path)],
            recursive=include_subdirs,
            extract_private=extract_private
        )

        # Language-specific optimizations
        lang_settings = {
            "c": {"optimize_output_for_c": True, "file_patterns": ["*.c", "*.h"]},
            "cpp": {"file_patterns": ["*.cpp", "*.hpp", "*.cc", "*.hh", "*.cxx", "*.hxx"]},
            "python": {"optimize_output_java": True, "file_patterns": ["*.py"]},
            "php": {"file_patterns": ["*.php", "*.php3", "*.inc"]},
            "java": {"optimize_output_java": True, "file_patterns": ["*.java"]},
            "csharp": {"file_patterns": ["*.cs"]},
            "javascript": {"file_patterns": ["*.js", "*.jsx", "*.ts", "*.tsx"]},
        }

        if language in lang_settings:
            for key, value in lang_settings[language].items():
                setattr(config, key, value)

        # Save configuration
        doxyfile_path = safe_project_path / "Doxyfile"
        with open(doxyfile_path, 'w', encoding='utf-8') as f:
            f.write(config.to_doxyfile())

        # Update .gitignore.md
        update_ignore_file(safe_project_path, "docs/")

        return f"✅ Doxygen project '{project_name}' created successfully at {safe_project_path} (Language: {language})"

    except Exception as e:
        return f"❌ Failed to create project: {str(e)}"

@mcp.tool()
async def generate_documentation(
    project_path: Optional[str] = None,
    output_format: str = "html",
    verbose: bool = False,
) -> str:
    """Generate documentation from source code using Doxygen"""
    try:
        safe_project_path = resolve_project_path(project_path)
    except ValueError as e:
        return f"❌ {str(e)}"

    doxyfile_path = safe_project_path / "Doxyfile"
    if not doxyfile_path.exists():
        return "❌ No Doxyfile found. Run 'auto_configure' or 'create_doxygen_project' first."

    doxygen_exe = os.environ.get("DOXYGEN_PATH", "doxygen")

    try:
        # Run Doxygen
        result = subprocess.run(
            [doxygen_exe, str(doxyfile_path)],
            cwd=str(safe_project_path),
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            return f"✅ Documentation generated successfully at {safe_project_path / 'docs' / 'html' / 'index.html'}"
        else:
            return f"❌ Documentation generation failed:\n{result.stderr or result.stdout}"

    except Exception as e:
        return f"❌ Error generating documentation: {str(e)}"

@mcp.tool()
async def scan_project(
    project_path: Optional[str] = None,
) -> str:
    """Analyze project structure and identify documentation opportunities"""
    try:
        safe_project_path = resolve_project_path(project_path)
    except ValueError as e:
        return f"❌ {str(e)}"

    if not safe_project_path.exists():
        return f"❌ Project path does not exist: {safe_project_path}"

    extensions = {}
    total_files = 0

    for file_path in safe_project_path.rglob("*"):
        if file_path.is_file() and not any(part.startswith('.') for part in file_path.parts):
            ext = file_path.suffix.lower()
            if ext:
                extensions[ext] = extensions.get(ext, 0) + 1
                total_files += 1

    sorted_extensions = sorted(extensions.items(), key=lambda x: x[1], reverse=True)
    result_text = f"📁 Project Scan Results: {safe_project_path}\n📊 Total Files: {total_files}\n\n📋 Files by Type:\n"
    for ext, count in sorted_extensions[:10]:
        result_text += f"  📄 {ext}: {count} files\n"

    return result_text

@mcp.tool()
async def query_project_reference(
    symbol_name: str,
    project_path: Optional[str] = None,
) -> str:
    """
    Search for documentation of a specific class, function, or namespace using XML output.
    """
    try:
        resolved_path = resolve_project_path(project_path)
        xml_dir = os.environ.get("DOXYGEN_XML_DIR")

        if not xml_dir:
            potential_paths = [
                resolved_path / "docs" / "xml",
                resolved_path / "xml",
            ]
            for p in potential_paths:
                if p.exists() and (p / "index.xml").exists():
                    xml_dir = str(p)
                    break

        if not xml_dir:
            return "❌ Error: Could not find Doxygen XML directory. Ensure XML generation is enabled in Doxyfile and documentation has been generated."

        engine = DoxygenQueryEngine(xml_dir)
        result = engine.query_symbol(symbol_name)

        if not result:
            return f"❓ Symbol '{symbol_name}' not found."

        output = f"🔍 Documentation for {result['kind']} {result['name']}\n"
        output += "=" * len(output) + "\n\n"
        if result["brief"]: output += f"Brief: {result['brief']}\n\n"
        if result["detailed"]: output += f"Detailed:\n{result['detailed']}\n\n"

        return output
    except Exception as e:
        return f"❌ Error querying symbol: {str(e)}"

@mcp.tool()
async def get_project_structure(project_path: Optional[str] = None) -> Dict[str, Any]:
    """
    Provide a tree-like overview of the project's documented components.
    """
    try:
        resolved_path = resolve_project_path(project_path)
        xml_dir = _find_xml_dir(resolved_path)

        if not xml_dir:
            return {"error": "Doxygen XML not found. Generate documentation first."}

        engine = DoxygenQueryEngine(xml_dir)

        structure = {
            "project_root": str(resolved_path),
            "classes": engine.list_all_symbols(kind_filter="class"),
            "namespaces": engine.list_all_symbols(kind_filter="namespace"),
            "files": engine.list_all_symbols(kind_filter="file"),
        }

        return structure
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
async def refresh_index(project_path: Optional[str] = None) -> str:
    """
    Trigger a re-scan/parse of Doxygen XML files.
    """
    try:
        resolved_path = resolve_project_path(project_path)
        xml_dir = _find_xml_dir(resolved_path)

        if not xml_dir:
            return "❌ Doxygen XML not found. Generate documentation first."

        # Re-initializing the engine effectively refreshes the index
        DoxygenQueryEngine(xml_dir)
        return "✅ Doxygen index refreshed successfully."
    except Exception as e:
        return f"❌ Error refreshing index: {str(e)}"

@mcp.tool()
async def get_symbol_at_location(file_path: str, line_number: int, project_path: Optional[str] = None) -> Optional[Dict[str, Any]]:
    """
    Find symbol context for the IDE's cursor.
    """
    try:
        resolved_path = resolve_project_path(project_path)
        xml_dir = _find_xml_dir(resolved_path)

        if not xml_dir:
            return {"error": "Doxygen XML not found. Generate documentation first."}

        engine = DoxygenQueryEngine(xml_dir)
        file_symbols = engine.get_file_structure(file_path)

        # Simple heuristic: find the symbol that contains this line
        best_match = None
        min_distance = float('inf')

        for symbol in file_symbols:
            loc = symbol.get("location", {})
            if loc.get("file") and Path(loc["file"]).name == Path(file_path).name:
                sym_line = int(loc.get("line", 0))
                if sym_line > 0 and sym_line <= line_number:
                    distance = line_number - sym_line
                    if distance < min_distance:
                        min_distance = distance
                        best_match = symbol

        return best_match
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
async def get_file_structure(file_path: str, project_path: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Retrieve all symbols defined in a specific file.
    """
    try:
        resolved_path = resolve_project_path(project_path)
        xml_dir = _find_xml_dir(resolved_path)

        if not xml_dir:
            return [{"error": "Doxygen XML not found. Generate documentation first."}]

        engine = DoxygenQueryEngine(xml_dir)
        return engine.get_file_structure(file_path)
    except Exception as e:
        return [{"error": str(e)}]

def _find_xml_dir(resolved_path: Path) -> Optional[str]:
    """
    Find the Doxygen XML directory with preference for:
    1. DOXYGEN_XML_DIR env var (absolute or relative)
    2. Standard locations within project root
    """
    xml_dir_env = os.environ.get("DOXYGEN_XML_DIR")
    if xml_dir_env:
        path = Path(xml_dir_env)
        if not path.is_absolute():
            path = resolved_path / path

        if path.exists() and (path / "index.xml").exists():
            return str(path.absolute())

    # Discovery in standard locations
    potential_paths = [
        resolved_path / "docs" / "xml",
        resolved_path / "xml",
        resolved_path / "doxygen" / "xml",
    ]
    for p in potential_paths:
        if p.exists() and (p / "index.xml").exists():
            return str(p.absolute())

    return None


def main():
    # Check for Doxygen dependency
    doxygen_exe = os.environ.get("DOXYGEN_PATH", "doxygen")
    try:
        subprocess.run([doxygen_exe, "--version"], capture_output=True, check=True)
    except (FileNotFoundError, subprocess.CalledProcessError):
        logger.warning(f"Doxygen not found at '{doxygen_exe}'. Attempting automatic setup...")
        script_path = Path(__file__).parent.parent.parent / "scripts" / "check_environment.py"
        try:
            subprocess.run([sys.executable, str(script_path), "--install"], check=True)
            # Re-verify after install
            subprocess.run([doxygen_exe, "--version"], capture_output=True, check=True)
            logger.info("Doxygen successfully installed and verified.")
        except Exception as e:
            logger.error(f"Automatic setup failed or Doxygen still not found: {e}")
            logger.error("Please install Doxygen manually: https://www.doxygen.nl/download.html")
            # We continue anyway to let MCP start, but tools will fail gracefully.

    mcp.run()

if __name__ == "__main__":
    main()
