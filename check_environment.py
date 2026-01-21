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

def test_doxygen_installation():
    """Test if Doxygen is installed and accessible"""
    print("Testing Doxygen installation...")
    doxygen_exe = os.environ.get("DOXYGEN_PATH", "doxygen")
    try:
        result = subprocess.run([doxygen_exe, "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            version = result.stdout.strip()
            print(f"[PASS] Doxygen {version} is installed and working at '{doxygen_exe}'!")
            return True
        else:
            print(f"[FAIL] Doxygen at '{doxygen_exe}' is not working properly")
            print(f"Error: {result.stderr}")
            return False
    except FileNotFoundError:
        print(f"[FAIL] Doxygen is not installed or not in PATH (checked '{doxygen_exe}')")
        print("Please install Doxygen or set DOXYGEN_PATH.")
        return False

def test_graphviz_installation():
    """Test if Graphviz (dot) is installed"""
    print("\nTesting Graphviz (dot) installation...")
    try:
        result = subprocess.run(["dot", "-V"], capture_output=True, text=True)
        if result.returncode == 0:
            version_info = result.stderr.strip()
            print(f"[PASS] Graphviz found: {version_info}")
            return True
        else:
            print("[FAIL] Graphviz dot command failed")
            return False
    except FileNotFoundError:
        print("[WARN] Graphviz (dot) not found - diagrams will not be generated")
        print("Install from: https://graphviz.org/download/")
        return True # Not a fatal fail

def test_python_dependencies():
    """Test if required Python packages are available"""
    print("\nTesting Python dependencies...")
    required_packages = ['mcp', 'pydantic']
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
        return False
    return True

def test_project_structure():
    """Test if all required project files are present"""
    print("\nTesting project structure...")

    project_root = Path(__file__).parent
    required_files = [
        'src/doxygen_mcp/server.py',
        'pyproject.toml',
        'package.json',
        'README.md',
        'templates/minimal.doxyfile',
        'templates/standard.doxyfile',
    ]

    missing_files = []
    for file_path in required_files:
        full_path = project_root / file_path
        if full_path.exists():
            print(f"[PASS] {file_path}")
        else:
            print(f"[FAIL] {file_path}")
            missing_files.append(file_path)

    if missing_files:
        print(f"\n[WARN] Missing files: {', '.join(missing_files)}")
        return False
    return True

def test_example_project():
    """Test the example C++ project"""
    print("\nTesting example C++ project...")

    project_root = Path(__file__).parent
    example_path = project_root / "examples" / "cpp_sample"

    if not example_path.exists():
        print(f"[FAIL] Example project path not found: {example_path}")
        return False

    cpp_files = list(example_path.glob("*.cpp"))
    h_files = list(example_path.glob("*.h"))

    print(f"Found {len(cpp_files)} .cpp files")
    print(f"Found {len(h_files)} .h files")

    documented_files = 0
    for file_path in cpp_files + h_files:
        content = file_path.read_text(encoding='utf-8')
        if '/**' in content or '///' in content or '@brief' in content:
            documented_files += 1
            print(f"[PASS] {file_path.name} has Doxygen comments")
        else:
            print(f"[WARN] {file_path.name} lacks Doxygen comments")

    total_files = len(cpp_files) + len(h_files)
    if total_files > 0:
        print(f"Documentation coverage: {documented_files}/{total_files} files")
        return documented_files > 0
    else:
        print("[FAIL] No source files found in example project")
        return False

def test_manual_doxygen_run():
    """Test running Doxygen manually on the example project"""
    print("\nTesting manual Doxygen run...")

    project_root = Path(__file__).parent
    example_path = project_root / "examples" / "cpp_sample"
    if not example_path.exists():
        return False

    safe_example_path = Path(os.path.abspath(os.path.realpath(example_path)))

    doxyfile_content = f"""
PROJECT_NAME           = "Calculator Example Test"
OUTPUT_DIRECTORY       = "{example_path}/test_docs"
INPUT                  = {example_path}
FILE_PATTERNS          = *.h *.cpp
RECURSIVE              = NO
GENERATE_HTML          = YES
GENERATE_LATEX         = NO
EXTRACT_ALL            = YES
SOURCE_BROWSER         = YES
"""

    doxyfile_path = example_path / "Doxyfile.test"
    doxyfile_path.write_text(doxyfile_content)

    try:
        print(f"Created test Doxyfile: {doxyfile_path}")
        doxygen_exe = os.environ.get("DOXYGEN_PATH", "doxygen")
        result = subprocess.run(
            [doxygen_exe, str(doxyfile_path)],
            cwd=example_path,
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print("[PASS] Doxygen ran successfully!")
            html_index = example_path / "test_docs" / "html" / "index.html"
            if html_index.exists():
                print(f"[PASS] HTML documentation created: {html_index}")
                return True
            else:
                print("[FAIL] HTML documentation not found")
                return False
        else:
            print("[FAIL] Doxygen failed to run")
            print(f"Error output: {result.stderr}")
            return False
    except Exception as e:
        print(f"[FAIL] Error running Doxygen test: {e}")
        return False
    finally:
        if doxyfile_path.exists():
            doxyfile_path.unlink()

def main():
    """Run all tests"""
    print("Doxygen MCP Server - Basic Functionality Tests")
    print("=" * 60)

    tests = [
        ("Doxygen Installation", test_doxygen_installation),
        ("Graphviz Installation", test_graphviz_installation),
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
    print("=" * 60)

    passed = 0
    for test_name, success in results:
        status = "[PASS]" if success else "[FAIL]"
        print(f"{status} {test_name}")
        if success:
            passed += 1

    print(f"\nOverall: {passed}/{len(results)} tests passed")
    return passed == len(results)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
