"""
Utility functions for Doxygen MCP context discovery and environment integration.
"""

import os
import json
from pathlib import Path
from typing import Optional, List, Dict, Any

def find_project_root(start_path: Path, markers: Optional[List[str]] = None) -> Path:
    """
    Search upwards from start_path for project markers to identify the workspace root.
    """
    if markers is None:
        markers = [
            ".git", ".svn", "Doxyfile", "pyproject.toml", "package.json",
            "CMakeLists.txt", "Makefile", "solution.sln", "go.mod", "Cargo.toml"
        ]

    current = start_path.resolve()
    for parent in [current] + list(current.parents):
        for marker in markers:
            if (parent / marker).exists():
                return parent

    return current

def resolve_project_path(project_path: Optional[str] = None) -> Path:
    """
    Resolve project path with priority:
    1. Explicit argument
    2. DOXYGEN_PROJECT_ROOT env var
    3. IDE-supplied workspace variables (VSCODE_WORKSPACE_FOLDER, etc.)
    4. Discovery via markers (searching up from CWD/PWD)
    """
    if project_path:
        return Path(os.path.abspath(os.path.realpath(project_path)))

    # Priority 2: Standard override
    env_root = os.environ.get("DOXYGEN_PROJECT_ROOT")
    if env_root:
        return Path(os.path.abspath(os.path.realpath(env_root)))

    # Priority 3: IDE Workspace variables
    ide_roots = [
        "VSCODE_WORKSPACE_FOLDER",
        "CURSOR_WORKSPACE_PATH",
        "PWD", # Often set by shells/IDE terminals
    ]
    for env_var in ide_roots:
        val = os.environ.get(env_var)
        if val and os.path.isdir(val):
            return Path(os.path.abspath(os.path.realpath(val)))

    # Priority 4: Search upwards from CWD
    return find_project_root(Path.cwd())


def detect_primary_language(project_path: Path) -> str:
    """
    Identify the dominant programming language in the project to optimize Doxygen settings.
    """
    ext_map = {
        ".cpp": "cpp", ".hpp": "cpp", ".cc": "cpp", ".hh": "cpp", ".cxx": "cpp",
        ".c": "c", ".h": "c",
        ".py": "python",
        ".php": "php",
        ".java": "java",
        ".cs": "csharp",
        ".js": "javascript", ".ts": "javascript", ".jsx": "javascript", ".tsx": "javascript",
        ".go": "go",
        ".rs": "rust"
    }

    counts = {}
    try:
        # Scan root and one level deep for performance
        files = list(project_path.glob("*")) + list(project_path.glob("*/*"))
        for f in files:
            if f.is_file():
                ext = f.suffix.lower()
                if ext in ext_map:
                    lang = ext_map[ext]
                    counts[lang] = counts.get(lang, 0) + 1
    except Exception:
        pass

    if not counts:
        return "mixed"

    return max(counts, key=counts.get)

def get_project_name(resolved_path: Path) -> str:
    """
    Attempt to determine the project name from the environment or project structure.
    """
    # Priority 1: standard env override
    env_name = os.environ.get("DOXYGEN_PROJECT_NAME")
    if env_name:
        return env_name

    # Priority 2: IDE specific variables
    ide_name_vars = [
        "VSCODE_WORKSPACE_NAME",
        "CURSOR_PROJECT_NAME",
        "PROJECT_NAME",
    ]
    for var in ide_name_vars:
        val = os.environ.get(var)
        if val:
            return val

    # Priority 3: Derived from workspace root folder name
    return resolved_path.name

def get_ide_environment() -> Dict[str, Any]:
    """
    Detect if the server is running within a specific IDE and extract relevant context.
    """
    project_root = resolve_project_path()
    context = {
        "ide": "unknown",
        "workspace_root": str(project_root),
        "project_name": get_project_name(project_root)
    }

    # VS Code / Cursor detection
    term_program = os.environ.get("TERM_PROGRAM")
    is_vscode = term_program == "vscode" or os.environ.get("VSCODE_GIT_IPC_HANDLE")

    if is_vscode:
        context["ide"] = "vscode"
        if os.environ.get("CURSOR_GIT_IPC_HANDLE") or "cursor" in os.environ.get("APP_PATH", "").lower():
            context["ide"] = "cursor"

        # Try to find VS Code settings
        vscode_settings = project_root / ".vscode" / "settings.json"
        if vscode_settings.exists():
            try:
                with open(vscode_settings, "r") as f:
                    context["vscode_settings"] = json.load(f)
            except:
                pass

    # JetBrains detection
    if os.environ.get("TERMINAL_EMULATOR") == "JetBrains-JediTerm":
        context["ide"] = "jetbrains"

    return context


def get_active_context() -> Dict[str, Any]:
    """
    Retrieve active file information if provided by the environment.
    Some MCP clients or IDE extensions might inject these into the environment.
    """
    return {
        "active_file": os.environ.get("MCP_ACTIVE_FILE"),
        "cursor_line": os.environ.get("MCP_CURSOR_LINE"),
        "cursor_column": os.environ.get("MCP_CURSOR_COLUMN"),
        "selected_text": os.environ.get("MCP_SELECTED_TEXT")
    }

def update_ignore_file(project_root: Path, path_to_ignore: str) -> bool:
    """
    Ensure a path is added to the project-specific .gitignore.md file.
     Returns True if an entry was added, False otherwise.
    """
    ignore_file = project_root / ".gitignore.md"
    new_entry = f"{path_to_ignore}\n"

    # Create file if it doesn't exist
    if not ignore_file.exists():
        try:
            with open(ignore_file, "w", encoding="utf-8") as f:
                f.write("# Doxygen Generated Documentation Folders\n")
                f.write(new_entry)
            return True
        except Exception:
            return False

    # Check if already ignored
    try:
        with open(ignore_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            if any(line.strip() == path_to_ignore.strip() for line in lines):
                return False

        # Append new entry
        with open(ignore_file, "a", encoding="utf-8") as f:
            if lines and not lines[-1].endswith("\n"):
                f.write("\n")
            f.write(new_entry)
        return True
    except Exception:
        return False
