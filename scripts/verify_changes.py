
import os
import sys
import asyncio
from pathlib import Path
from unittest.mock import patch

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))

from doxygen_mcp.server import _resolve_project_path, create_doxygen_project

def test_resolve_logic():
    print("Testing _resolve_project_path...")
    
    # Test 1: Explicit path
    p = _resolve_project_path("foo")
    assert p.name == "foo"
    print("  Explicit path: OK")
    
    # Test 2: Env var
    os.environ["DOXYGEN_PROJECT_ROOT"] = str(Path("bar").resolve())
    p = _resolve_project_path(None)
    assert p.name == "bar"
    print("  Env var: OK")
    
    # Test 3: Missing
    del os.environ["DOXYGEN_PROJECT_ROOT"]
    try:
        _resolve_project_path(None)
        print("  Missing path: FAILED (should raise)")
    except ValueError:
        print("  Missing path: OK")

async def test_tools():
    print("\nTesting tools...")
    
    # Setup
    test_dir = Path("test_verify_env").resolve()
    if test_dir.exists():
        import shutil
        shutil.rmtree(test_dir)
    
    os.environ["DOXYGEN_PROJECT_ROOT"] = str(test_dir)
    
    # Test create_doxygen_project with implicit path
    print("  Running create_doxygen_project(project_path=None)...")
    try:
        result = await create_doxygen_project(
            project_name="Verify Project",
            # project_path defaults to None
            language="python"
        )
        
        if "✅" in result:
            print("  Creation: OK")
        else:
            print(f"  Creation: FAILED - {result.encode('utf-8', errors='replace')}")
            
        if (test_dir / "Doxyfile").exists():
            print("  Doxyfile check: OK")
        else:
            print("  Doxyfile check: FAILED")
            
    except Exception as e:
        print(f"  Exception during tool call: {e}")


    # Clean up
    import shutil
    if test_dir.exists():
        shutil.rmtree(test_dir)

if __name__ == "__main__":
    test_resolve_logic()
    asyncio.run(test_tools())
