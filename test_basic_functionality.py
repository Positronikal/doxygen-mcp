#!/usr/bin/env python3
"""
Basic functionality test for Doxygen MCP Server
Run this script to verify core functionality before MCP integration
"""

import subprocess
import sys
from pathlib import Path
import json

def test_doxygen_installation():
    """Test if Doxygen is installed and accessible"""
    print("🔍 Testing Doxygen installation...")
    try:
        result = subprocess.run(["doxygen", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            version = result.stdout.strip()
            print(f"✅ Doxygen {version} is installed and working!")
            return True
        else:
            print("❌ Doxygen is not working properly")
            print(f"Error: {result.stderr}")
            return False
    except FileNotFoundError:
        print("❌ Doxygen is not installed or not in PATH")
        print("Please install Doxygen from: https://www.doxygen.nl/download.html")
        return False

def test_graphviz_installation():
    """Test if Graphviz (dot) is installed"""
    print("\n🔍 Testing Graphviz (dot) installation...")
    try:
        result = subprocess.run(["dot", "-V"], capture_output=True, text=True)
        if result.returncode == 0:
            # Graphviz outputs version to stderr
            version_info = result.stderr.strip()
            print(f"✅ Graphviz found: {version_info}")
            return True
        else:
            print("❌ Graphviz dot command failed")
            return False
    except FileNotFoundError:
        print("⚠️ Graphviz (dot) not found - diagrams will not be generated")
        print("Install from: https://graphviz.org/download/")
        return False

def test_python_dependencies():
    """Test if required Python packages are available"""
    print("\n🔍 Testing Python dependencies...")
    required_packages = ['mcp', 'pydantic']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package} is available")
        except ImportError:
            print(f"❌ {package} is missing")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n⚠️ Missing packages: {', '.join(missing_packages)}")
        print("Install with: pip install -r requirements.txt")
        return False
    return True

def test_project_structure():
    """Test if all required project files are present"""
    print("\n🔍 Testing project structure...")
    
    project_root = Path(__file__).parent
    required_files = [
        'server.py',
        'requirements.txt',
        'package.json',
        'README.md',
        'templates/minimal.doxyfile',
        'templates/standard.doxyfile',
        'templates/comprehensive.doxyfile',
        'examples/cpp_sample/calculator.h',
        'examples/cpp_sample/calculator.cpp'
    ]
    
    missing_files = []
    for file_path in required_files:
        full_path = project_root / file_path
        if full_path.exists():
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path}")
            missing_files.append(file_path)
    
    if missing_files:
        print(f"\n⚠️ Missing files: {', '.join(missing_files)}")
        return False
    return True

def test_example_project():
    """Test the example C++ project"""
    print("\n🔍 Testing example C++ project...")
    
    project_root = Path(__file__).parent
    example_path = project_root / "examples" / "cpp_sample"
    
    # Count source files
    cpp_files = list(example_path.glob("*.cpp"))
    h_files = list(example_path.glob("*.h"))
    
    print(f"📄 Found {len(cpp_files)} .cpp files")
    print(f"📄 Found {len(h_files)} .h files")
    
    # Check if files have Doxygen comments
    documented_files = 0
    for file_path in cpp_files + h_files:
        content = file_path.read_text(encoding='utf-8')
        if '/**' in content or '///' in content or '@brief' in content:
            documented_files += 1
            print(f"✅ {file_path.name} has Doxygen comments")
        else:
            print(f"⚠️ {file_path.name} lacks Doxygen comments")
    
    total_files = len(cpp_files) + len(h_files)
    if total_files > 0:
        print(f"📊 Documentation coverage: {documented_files}/{total_files} files")
        return documented_files > 0
    else:
        print("❌ No source files found in example project")
        return False

def test_manual_doxygen_run():
    """Test running Doxygen manually on the example project"""
    print("\n🔍 Testing manual Doxygen run...")
    
    project_root = Path(__file__).parent
    example_path = project_root / "examples" / "cpp_sample"
    
    # Create a simple Doxyfile for testing
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
        print(f"📝 Created test Doxyfile: {doxyfile_path}")
        
        # Run Doxygen
        result = subprocess.run(
            ["doxygen", str(doxyfile_path)],
            cwd=example_path,
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print("✅ Doxygen ran successfully!")
            
            # Check if HTML output was created
            html_index = example_path / "test_docs" / "html" / "index.html"
            if html_index.exists():
                print(f"✅ HTML documentation created: {html_index}")
                print(f"📊 Documentation size: {html_index.stat().st_size} bytes")
                return True
            else:
                print("❌ HTML documentation not found")
                return False
        else:
            print("❌ Doxygen failed to run")
            print(f"Error output: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Error running Doxygen test: {e}")
        return False
    finally:
        # Clean up
        if doxyfile_path.exists():
            doxyfile_path.unlink()

def main():
    """Run all tests"""
    print("🚀 Doxygen MCP Server - Basic Functionality Tests")
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
            print(f"❌ {test_name} failed with exception: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 Test Results Summary:")
    print("=" * 60)
    
    passed = 0
    for test_name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} {test_name}")
        if success:
            passed += 1
    
    print(f"\n🎯 Overall: {passed}/{len(results)} tests passed")
    
    if passed == len(results):
        print("\n🎉 All tests passed! Ready for MCP integration testing.")
        return True
    else:
        print(f"\n⚠️ {len(results) - passed} tests failed. Please address issues before proceeding.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
