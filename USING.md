# Using
Detailed documentation located in `docs/` elsewhere in this repo.

## Installation

### Prerequisites
1. **Doxygen** (required)
   ```bash
   # Ubuntu/Debian
   sudo apt-get install doxygen
   
   # macOS
   brew install doxygen
   
   # Windows
   # Download from https://www.doxygen.nl/download.html
   ```

2. **Graphviz** (optional, for diagram generation)
   ```bash
   # Ubuntu/Debian
   sudo apt-get install graphviz
   
   # macOS
   brew install graphviz
   
   # Windows
   # Download from https://graphviz.org/download/
   ```

3. **LaTeX** (optional, for PDF generation)
   ```bash
   # Ubuntu/Debian
   sudo apt-get install texlive-full
   
   # macOS
   brew install --cask mactex
   
   # Windows
   # Download MiKTeX from https://miktex.org/
   ```

### Server Installation
1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd doxygen-mcp
   ```

2. **Install Python dependencies**
   We recommend using [uv](https://docs.astral.sh/uv/) to manage your Python projects.
   ```bash
   # Create a virtual environment
   uv venv

   # Activate the virtual environment
   source .venv/bin/activate

   # Install dependencies
   uv pip install -e .[dev]
   ```

3. **Verify installation**
   ```bash
   doxygen-mcp-server --help
   ```

## Starting the Server
```bash
# Start the MCP server
doxygen-mcp-server
```

## Running with uvenv
This project is configured to be run with `uvenv` for MCP clients. To run the server with `uvenv`, you will need to have `uvenv` installed. You can then run the server using the following command:
```bash
uvenv doxygen-mcp-server
```

The server communicates via stdin/stdout using the MCP protocol.

## Available Tools
The server provides the following tools for documentation management:

### Project Management
- `create_doxygen_project` - Initialize a new documentation project
- `scan_project` - Analyze project structure and identify files
- `suggest_file_patterns` - Get recommendations for file inclusion patterns

### Documentation Generation
- `generate_documentation` - Create documentation from source code
- `validate_documentation` - Check for warnings and coverage issues
- `export_documentation` - Export docs in various formats

### Configuration
- `create_doxyfile` - Generate Doxygen configuration files
- `parse_doxyfile` - Analyze existing configurations
- `configure_project` - Modify project settings

### Analysis & Utilities
- `analyze_coverage` - Detailed documentation coverage analysis
- `extract_api_structure` - Parse and analyze API structure
- `generate_diagrams` - Create specific diagram types
- `check_doxygen_install` - Verify system requirements

## Example Workflow
1. **Create a new project**
   ```json
   {
     "tool": "create_doxygen_project",
     "arguments": {
       "project_name": "My API Documentation",
       "project_path": "/path/to/my/project",
       "language": "cpp",
       "include_subdirs": true,
       "extract_private": false
     }
   }
   ```

2. **Scan existing codebase**
   ```json
   {
     "tool": "scan_project",
     "arguments": {
       "project_path": "/path/to/my/project",
       "language_filter": ["cpp", "h"],
       "exclude_patterns": ["*/build/*", "*/test/*"]
     }
   }
   ```

3. **Generate documentation**
   ```json
   {
     "tool": "generate_documentation",
     "arguments": {
       "project_path": "/path/to/my/project",
       "output_format": "html",
       "clean_output": true,
       "verbose": false
     }
   }
   ```

4. **Validate documentation quality**
   ```json
   {
     "tool": "validate_documentation",
     "arguments": {
       "project_path": "/path/to/my/project",
       "check_coverage": true,
       "warn_undocumented": true,
       "output_format": "text"
     }
   }
   ```

## Configuration Templates
The server provides three configuration templates:

### Minimal Template
- Basic HTML output only
- Public members only
- No diagrams
- Suitable for quick documentation

### Standard Template (Default)
- HTML and XML output
- Public and protected members
- Basic diagrams
- Balanced feature set

### Comprehensive Template
- All output formats enabled
- All members included (public, protected, private)
- Full diagram generation
- Maximum documentation features

## Language-Specific Features

### C/C++ Projects
- Automatic header/implementation file detection
- Class hierarchy diagrams
- Include dependency graphs
- Preprocessor macro documentation

### Python Projects
- Docstring parsing
- Module structure analysis
- Package documentation
- Cross-references between modules

### Java Projects
- Package documentation
- Javadoc compatibility
- Inheritance diagrams
- Interface documentation

### PHP Projects
- Namespace support
- Class and function documentation
- PHPDoc tag support

## Advanced Features

### Diagram Generation
- **Class Diagrams**: Show class relationships and hierarchies
- **Collaboration Diagrams**: Display class interactions
- **Call Graphs**: Visualize function call relationships
- **Include Graphs**: Show file dependency relationships
- **Directory Structure**: Project organization visualization

### Documentation Analysis
- **Coverage Analysis**: Identify undocumented code elements
- **Warning Detection**: Find documentation inconsistencies
- **Quality Metrics**: Measure documentation completeness
- **Cross-Reference Validation**: Verify internal links

### Multi-Format Output
- **HTML**: Interactive web documentation with search
- **PDF**: Print-ready documentation via LaTeX
- **XML**: Machine-readable structured output
- **Man Pages**: Unix manual page format
- **RTF**: Microsoft Word compatible format

## Integration with MCP Clients

### Claude Desktop Integration
Add to your MCP client configuration:

```json
{
  "mcpServers": {
    "doxygen-mcp": {
      "command": "python",
      "args": ["/path/to/doxygen-mcp/server.py"],
      "env": {}
    }
  }
}
```

### Custom MCP Client
```python
import mcp

# Connect to the Doxygen MCP server
client = mcp.Client()
await client.connect_stdio("python", ["/path/to/doxygen-mcp/server.py"])

# List available tools
tools = await client.list_tools()

# Create a new documentation project
result = await client.call_tool("create_doxygen_project", {
    "project_name": "My Project",
    "project_path": "/path/to/project",
    "language": "cpp"
})
```