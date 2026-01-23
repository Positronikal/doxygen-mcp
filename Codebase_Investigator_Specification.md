# Codebase Investigator: Operational Specification

## Purpose
The `codebase_investigator` is a specialized sub-agent designed to perform in-depth analysis of a software project's codebase. Its primary goal is to provide a structured understanding of the project's architecture, dependencies, and key components to facilitate complex software engineering tasks like bug fixing, feature implementation, and refactoring.

## Operational Flow (Conceptual):

### 1. Input
The `codebase_investigator` receives an `objective` from the main agent, detailing the specific aspects of the codebase to investigate (e.g., "analyze server configuration," "map architectural dependencies").

```python
# Conceptual input to the codebase_investigator
objective = {
    "task": "analyze_server_configuration",
    "details": "Identify current configuration mechanisms, state management, and IDE integration points for 'doxygen-mcp' server."
}
```

### 2. Codebase Traversal
It systematically traverses the project directory, identifying relevant files and directories. This involves:
*   Reading file system metadata.
*   Identifying common programming language file extensions.
*   Respecting `.gitignore` and other exclusion patterns to focus on relevant source code.

```python
import os
import fnmatch

def traverse_codebase(root_dir, ignore_patterns):
    """
    Conceptual function to traverse a codebase, respecting ignore patterns.
    """
    relevant_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if not any(fnmatch.fnmatch(file_path, pattern) for pattern in ignore_patterns):
                relevant_files.append(file_path)
    return relevant_files

# Example usage (conceptual)
# ignore_list = ['.git/', '.venv/', '__pycache__/', '*.pyc']
# project_files = traverse_codebase("C:\\github\\tools\\doxygen-mcp", ignore_list)
# print(f"Found {len(project_files)} relevant files.")
```

### 3. Static Analysis
Performs static analysis on the identified source code files without executing them. This includes:

*   **Dependency Mapping:** Identifying import statements, function calls, and class relationships across files to build a dependency graph.
*   **Architectural Pattern Recognition:** Detecting common architectural patterns (e.g., MVC, client-server, microservices) based on file organization, naming conventions, and inter-module communication.
*   **Configuration Analysis:** Locating and parsing configuration files (e.g., `.json`, `.yaml`, `.ini`, code-based configurations) to understand how the application is set up.
*   **Symbol Extraction:** Identifying key functions, classes, variables, and their definitions/usages.
*   **Contextual Understanding:** Analyzing surrounding code, comments, and documentation to infer the purpose and behavior of different code sections.

```python
import re

def analyze_python_file(file_path):
    """
    Conceptual function for static analysis of a Python file.
    Extracts imports and class/function definitions.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    imports = re.findall(r'^\s*(?:import|from)\s+([a-zA-Z0-9_.]+)', content, re.MULTILINE)
    classes = re.findall(r'^\s*class\s+([a-zA-Z0-9_]+)', content, re.MULTILINE)
    functions = re.findall(r'^\s*def\s+([a-zA-Z0-9_]+)\s*\(', content, re.MULTILINE)

    config_patterns = re.findall(r'([A-Z_]+)\s*=\s*(.+)', content) # Simple config variable detection

    return {
        "file": file_path,
        "imports": imports,
        "classes": classes,
        "functions": functions,
        "potential_configs": config_patterns
    }

# Example usage (conceptual)
# analysis_results = analyze_python_file("C:\\github\\tools\\doxygen-mcp\\src\\doxygen_mcp\\server.py")
# print(analysis_results)
```

### 4. Information Synthesis
Synthesizes the gathered information into a coherent model of the codebase relevant to the given objective. This involves:
*   Prioritizing information based on the initial request's focus.
*   Identifying key file paths, symbols, and architectural insights.
*   Detecting potential areas for modification or improvement.

```python
def synthesize_report(analysis_data, objective):
    """
    Conceptual function to synthesize analysis data into a report based on the objective.
    """
    report = {"summary": f"Analysis report for objective: {objective['task']}"}
    config_findings = []
    state_management_findings = []

    for data in analysis_data:
        if "config" in data.get("file", "").lower() or "doxyfile" in data.get("file", "").lower():
            config_findings.append(data)
        # More sophisticated logic here to identify state management or IDE integration
        # ...

    report["configuration_details"] = config_findings
    report["potential_ide_integration_points"] = [] # Placeholder
    report["codebase_state_tracking"] = [] # Placeholder

    return report

# Example usage (conceptual)
# synthetic_report = synthesize_report(list_of_analysis_results, objective)
# print(synthetic_report)
```

### 5. Output
Generates a structured report that includes:
*   Key file paths and their relevance.
*   Important symbols and their definitions/usages.
*   Architectural observations and insights.
*   Actionable recommendations or summaries based on the investigation objective.
*   Answers to specific questions posed in the objective.

```python
def generate_markdown_report(final_report):
    """
    Conceptual function to format the final report into Markdown.
    """
    markdown_output = f"# Codebase Investigator Report: {final_report['summary']}\n\n"
    markdown_output += "## Configuration Details\n"
    for config in final_report.get("configuration_details", []):
        markdown_output += f"- File: `{config['file']}`\n"
        markdown_output += f"  Potential Configs: {config.get('potential_configs', 'N/A')}\n"
    # ... more formatting based on report structure
    return markdown_output

# Example usage (conceptual)
# final_markdown = generate_markdown_report(synthetic_report)
# print(final_markdown)
```

## Key Capabilities:
*   **Holistic View:** Provides a comprehensive understanding of how different parts of the codebase interact.
*   **Targeted Analysis:** Can focus on specific aspects of the codebase as directed by the objective.
*   **Pattern Recognition:** Identifies common software engineering patterns and anti-patterns.
*   **Dependency Resolution:** Maps out internal and external dependencies.

## Limitations (as perceived by the calling agent):
*   Does not execute code; relies solely on static analysis.
*   Its internal algorithms are proprietary; the calling agent only interacts with its public interface and interprets its output.
*   May require several iterations or more specific objectives for highly nuanced or ambiguous analysis.

```
