import os
import sys
from pathlib import Path
from typing import List, Dict, Any

# Add src to path to import DoxygenQueryEngine
sys.path.append(str(Path("src").resolve()))
from doxygen_mcp.query_engine import DoxygenQueryEngine

# Force UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

def analyze_docs_coverage(xml_dir: str):
    print("# Documentation Coverage Report")
    print(f"\n**Analysis Target:** `{xml_dir}`")

    engine = DoxygenQueryEngine(xml_dir)

    # Get all classes
    classes = engine.list_all_symbols(kind_filter="class")
    print(f"\n- **Total Classes Found:** {len(classes)}")

    missing_docs = []

    for class_name in classes:
        details = engine.query_symbol(class_name)
        if not details or "error" in details:
            continue

        class_missing = []

        # Check class level docs
        if not details.get("brief") and not details.get("detailed"):
            class_missing.append("Class Description")

        # Check members
        members = details.get("members", [])
        for m in members:
            # Skip compiler generated or trivial members if possible
            if m["name"].startswith("~") or m["name"] == class_name:
                continue

            if not m.get("brief") and not m.get("detailed"):
                 class_missing.append(f"Member: `{m['name']}`")

        if class_missing:
            missing_docs.append({
                "name": class_name,
                "issues": class_missing
            })

    print("\n## 📉 Missing Documentation")
    print("| Class Name | Missing Items |")
    print("| :--- | :--- |")

    total_issues = 0

    for item in sorted(missing_docs, key=lambda x: x['name']):
        # Limit the number of issues shown per class to keep table readable
        issues = item['issues']
        total_issues += len(issues)

        display_issues = "<br>".join(issues[:5])
        if len(issues) > 5:
            display_issues += f"<br>...and {len(issues)-5} more"

        print(f"| `{item['name']}` | {display_issues} |")

    print(f"\n**Summary:** Found **{len(missing_docs)}** classes with missing documentation, totaling **{total_issues}** undocumented items.")

if __name__ == "__main__":
    if "DOXYGEN_XML_DIR" not in os.environ:
        os.environ["DOXYGEN_XML_DIR"] = r"C:\GitHub\MidiKobold\xml"

    analyze_docs_coverage(os.environ["DOXYGEN_XML_DIR"])
