#!/usr/bin/env python3
"""
Basic functionality test for Doxygen MCP Server
Run this script to verify core functionality before MCP integration
"""

import subprocess
import sys
import os
from pathlib import Path
import json

def install_with_winget(package_id: str, name: str) -> bool:
    """Attempt to install a package using Windows Package Manager (winget)"""
    print(f"Attempting to install {name} via winget...")
    try:
        # Check if winget is available
        subprocess.run(["winget", "--version"], capture_output=True, check=True)

        # Install the package
        result = subprocess.run(
            ["winget", "install", "--id", package_id, "--exact", "--accept-package-agreements", "--accept-source-agreements"],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print(f"[PASS] Successfully installed {name}!")
            return True
        else:
            print(f"[FAIL] winget failed to install {name}.")
            print(f"Error: {result.stderr}")
            return False
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("[FAIL] winget is not available. Please install manually.")
        return False

def test_doxygen_installation(auto_install: bool = False):
    """Test if Doxygen is installed and accessible"""
    print("Testing Doxygen installation...")
    doxygen_exe = os.environ.get("DOXYGEN_PATH", "doxygen")
    try:
        result = subprocess.run([doxygen_exe, "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            version = result.stdout.strip()
            print(f"[PASS] Doxygen {version} is installed and working at '{doxygen_exe}'!")
            return True
    except FileNotFoundError:
        pass

    print(f"[FAIL] Doxygen is not installed or not in PATH (checked '{doxygen_exe}')")
    if auto_install and sys.platform == "win32":
        return install_with_winget("Doxygen.Doxygen", "Doxygen")

    print("Please install Doxygen or set DOXYGEN_PATH.")
    return False

def test_graphviz_installation(auto_install: bool = False):
    """Test if Graphviz (dot) is installed"""
    print("\nTesting Graphviz (dot) installation...")
    try:
        result = subprocess.run(["dot", "-V"], capture_output=True, text=True)
        if result.returncode == 0:
            version_info = result.stderr.strip()
            print(f"[PASS] Graphviz found: {version_info}")
            return True
    except FileNotFoundError:
        pass

    print("[WARN] Graphviz (dot) not found - diagrams will not be generated")
    if auto_install and sys.platform == "win32":
        return install_with_winget("Graphviz.Graphviz", "Graphviz")

    print("Install from: https://graphviz.org/download/")
    return True # Not a fatal fail for core functionality

def test_python_dependencies():
    """Test if required Python packages are available"""
    print("\nTesting Python dependencies...")
    required_packages = ['mcp', 'pydantic', 'lxml']
    missing_packages = []

    for package in required_packages:
        try:
            __import__(package)
            print(f"[PASS] {package} is available")
        except ImportError:
            print(f"[FAIL] {package} is missing")
            missing_packages.append(package)

    if missing_packages:
        print(f"\n[WARN] Missing packages: {', '.join(missing_packages)}")
        print("Try: uv sync OR pip install " + " ".join(missing_packages))
        return False
    return True

def test_project_structure():
    """Test if all required project files are present"""
    print("\nTesting project structure...")

    # Resolve project root relative to this script
    script_path = Path(__file__).resolve()
    project_root = script_path.parent.parent

    required_files = [
        'src/doxygen_mcp/server.py',
        'pyproject.toml',
        'README.md',
    ]

    missing_files = []
    for file_path in required_files:
        full_path = project_root / file_path
        if full_path.exists():
            print(f"[PASS] {file_path}")
        else:
            print(f"[FAIL] {file_path} (checked {full_path})")
            missing_files.append(file_path)

    if missing_files:
        print(f"\n[WARN] Missing files: {', '.join(missing_files)}")
        return False
    return True

def test_example_project():
    """Test the example C++ project"""
    print("\nTesting example C++ project...")

    script_path = Path(__file__).resolve()
    project_root = script_path.parent.parent
    example_path = project_root / "examples" / "cpp_sample"

    if not example_path.exists():
        print(f"[SKIP] Example project path not found: {example_path}")
        return True

    cpp_files = list(example_path.glob("*.cpp"))
    h_files = list(example_path.glob("*.h"))

    print(f"Found {len(cpp_files)} .cpp files, {len(h_files)} .h files")

    documented_files = 0
    for file_path in cpp_files + h_files:
        content = file_path.read_text(encoding='utf-8')
        if any(marker in content for marker in ['/**', '///', '@brief']):
            documented_files += 1

    total_files = len(cpp_files) + len(h_files)
    if total_files > 0:
        print(f"Documentation coverage: {documented_files}/{total_files} files")
        return documented_files > 0
    return True

def test_manual_doxygen_run():
    """Test running Doxygen manually on the example project"""
    print("\nTesting manual Doxygen run...")

    script_path = Path(__file__).resolve()
    project_root = script_path.parent.parent
    example_path = project_root / "examples" / "cpp_sample"
    if not example_path.exists():
        return True

    doxyfile_content = f"""
PROJECT_NAME           = "Calculator Example Test"
OUTPUT_DIRECTORY       = "test_docs"
INPUT                  = .
FILE_PATTERNS          = *.h *.cpp
RECURSIVE              = NO
GENERATE_XML           = YES
GENERATE_HTML          = NO
EXTRACT_ALL            = YES
"""

    doxyfile_path = example_path / "Doxyfile.test"
    doxyfile_path.write_text(doxyfile_content)

    try:
        doxygen_exe = os.environ.get("DOXYGEN_PATH", "doxygen")
        result = subprocess.run(
            [doxygen_exe, str(doxyfile_path)],
            cwd=example_path,
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print("[PASS] Doxygen ran successfully!")
            return True
        else:
            print("[FAIL] Doxygen failed to run")
            return False
    except Exception as e:
        print(f"[FAIL] Error running Doxygen test: {e}")
        return False
    finally:
        if doxyfile_path.exists():
            doxyfile_path.unlink()

def main(auto_install: bool = False):
    """Run all tests"""
    print("Doxygen MCP Server - Environment Check & Setup")
    print("=" * 60)

    tests = [
        ("Doxygen Installation", lambda: test_doxygen_installation(auto_install)),
        ("Graphviz Installation", lambda: test_graphviz_installation(auto_install)),
        ("Python Dependencies", test_python_dependencies),
        ("Project Structure", test_project_structure),
        ("Example Project", test_example_project),
        ("Manual Doxygen Run", test_manual_doxygen_run)
    ]

    results = []
    for test_name, test_func in tests:
        try:
            success = test_func()
            results.append((test_name, success))
        except Exception as e:
            print(f"[FAIL] {test_name} failed with exception: {e}")
            results.append((test_name, False))

    print("\n" + "=" * 60)
    print("Test Results Summary:")
    passed = 0
    for test_name, success in results:
        status = "[PASS]" if success else "[FAIL]"
        print(f"{status} {test_name}")
        if success: passed += 1

    print(f"\nOverall: {passed}/{len(results)} tests passed")
    return passed == len(results)

if __name__ == "__main__":
    auto = "--install" in sys.argv
    success = main(auto_install=auto)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
