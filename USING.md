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

2. **Install with uv (Recommended)**
   We use [uv](https://docs.astral.sh/uv/) for fast, modern Python dependency management.
   ```bash
   # Install dependencies and create virtual environment
   uv sync

   # For development dependencies
   uv sync --extra dev
   ```

3. **Verify installation**
   ```bash
   uv run doxygen-mcp --version
   ```

## Starting the Server
The server uses the MCP stdio transport and communicates via stdin/stdout.

```bash
# Start the MCP server
uv run doxygen-mcp
```

The server will run continuously, waiting for MCP protocol messages on stdin.

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

**Using uv (Recommended):**
```json
{
  "mcpServers": {
    "doxygen-mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/doxygen-mcp",
        "run",
        "doxygen-mcp"
      ],
      "env": {}
    }
  }
}
```

**Using installed package:**
```json
{
  "mcpServers": {
    "doxygen-mcp": {
      "command": "doxygen-mcp",
      "args": [],
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
await client.connect_stdio("uv", [
    "--directory", "/path/to/doxygen-mcp",
    "run", "doxygen-mcp"
])

# List available tools
tools = await client.list_tools()

# Create a new documentation project
result = await client.call_tool("create_doxygen_project", {
    "project_name": "My Project",
    "project_path": "/path/to/project",
    "language": "cpp"
})
```

## Environment Configuration

The server supports several environment variables to streamline your workflow and avoid repeating paths in every prompt. You can set these in your MCP client's configuration (e.g., `claude_desktop_config.json`).

### Key Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `DOXYGEN_PROJECT_ROOT` | Default path to your project source code. When set, tools like `create_doxygen_project` and `generate_documentation` will use this path by default if no `project_path` argument is provided. | `/home/user/projects/my-app` |
| `DOXYGEN_XML_DIR` | Explicit path to the directory containing Doxygen XML output (`index.xml`). Use this if your XML files are stored in a non-standard location or if you want to query documentation without specifying the project root. | `/home/user/projects/my-app/docs/xml` |
| `DOXYGEN_PATH` | Path to the Doxygen executable. Useful if `doxygen` is not in your system PATH. | `/usr/local/bin/doxygen` |

### Configuration Example

```json
{
  "mcpServers": {
    "doxygen-mcp": {
      "command": "uv",
      "args": ["run", "doxygen-mcp"],
      "env": {
        "DOXYGEN_PROJECT_ROOT": "C:\\Users\\Me\\Projects\\MyGame",
        "DOXYGEN_PATH": "C:\\Program Files\\doxygen\\bin\\doxygen.exe"
      }
    }
  }
}
```

## Development

### Running Tests

```bash
# Install development dependencies
uv sync --extra dev

# Run all tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=src/doxygen_mcp --cov-report=html

# Run specific test file
uv run pytest tests/test_server.py -v
```

### Code Quality

```bash
# Format code with black
uv run black src/doxygen_mcp/

# Type checking with mypy
uv run mypy src/doxygen_mcp/

# Run linting
uv run pylint src/doxygen_mcp/
```

### Running Server Manually

```bash
# Start server for MCP Inspector or debugging
uv run doxygen-mcp

# Or as module
uv run python -m doxygen_mcp
```

### Performance Optimization

For large projects, consider these Doxygen configuration optimizations:

- **`EXTRACT_ALL = NO`**: Reduce processing time by only documenting annotated code
- **`OPTIMIZE_OUTPUT_FOR_C = YES`**: Optimize for C projects (C-specific output)
- **`MAX_DOT_GRAPH_DEPTH`**: Limit diagram complexity to improve generation speed
- **`EXCLUDE_PATTERNS`**: Skip unnecessary files (build/, vendor/, node_modules/)
- **`USE_MDFILE_AS_MAINPAGE`**: Use README.md as the main documentation page

### Adding New Features

When extending the server with new tools:

1. **Extend Configuration**: Add new options to `DoxygenConfig` class if needed
2. **Implement Tool**: Add `@mcp.tool()` decorated function in `server.py`
3. **Add Validation**: Use Pydantic models for parameter validation
4. **Write Tests**: Create comprehensive test cases in `tests/`
5. **Update Documentation**: Document the new tool in this file
6. **Update Examples**: Add usage examples

### Project Structure

```
doxygen-mcp/
├── src/
│   └── doxygen_mcp/
│       ├── __init__.py       # Package initialization
│       ├── __main__.py       # Entry point
│       └── server.py         # Main server implementation
├── tests/
│   └── test_server.py        # Test suite
├── examples/                 # Example projects
├── templates/                # Doxyfile templates
├── pyproject.toml           # Project configuration
└── README.md                # Project overview
```

## Migration Guide

### Upgrading from Pre-1.0 Structure

If you're upgrading from an older version that used `server.py` at the root level:

#### What Changed

1. **Command Name**: `doxygen-mcp-server` → `doxygen-mcp`
2. **Package Structure**: Root `server.py` → `src/doxygen_mcp/`
3. **Installation**: `uv pip install` → `uv sync`
4. **Python Version**: `>=3.8` → `>=3.11`

#### Migration Steps

1. **Update Your Environment**
   ```bash
   # Pull latest changes
   git pull origin main

   # Remove old virtual environment
   rm -rf .venv

   # Install with new structure
   uv sync
   ```

2. **Update MCP Client Configuration**

   Change from:
   ```json
   {
     "command": "python",
     "args": ["/path/to/doxygen-mcp/server.py"]
   }
   ```

   To:
   ```json
   {
     "command": "uv",
     "args": [
       "--directory",
       "/path/to/doxygen-mcp",
       "run",
       "doxygen-mcp"
     ]
   }
   ```

3. **Update CI/CD Pipelines**

   Change from:
   ```bash
   pip install -r requirements.txt
   python server.py
   ```

   To:
   ```bash
   uv sync
   uv run doxygen-mcp
   ```

4. **Verify Migration**
   ```bash
   # Test server starts correctly
   timeout 3 uv run doxygen-mcp || echo "Success"

   # Verify package imports
   uv run python -c "import doxygen_mcp; print(doxygen_mcp.__version__)"
   ```

#### Breaking Changes

- **Command name changed**: Any scripts using `doxygen-mcp-server` must update
- **Import paths changed**: If extending the server, update imports:
  - Old: `from server import ...`
  - New: `from doxygen_mcp.server import ...`
- **Python 3.11+ required**: Older Python versions no longer supported

#### Backward Compatibility

The old `server.py` at the root is deprecated but still present temporarily. It will be removed in version 2.0.

#### Troubleshooting Migration

**"Module not found" errors:**
- Run `uv sync` to ensure dependencies are installed
- Verify you're in the project root directory

**"Command not found: doxygen-mcp":**
- Use `uv run doxygen-mcp` instead
- Or activate venv: `source .venv/bin/activate` (Linux/macOS) or `.venv\Scripts\activate` (Windows)

**MCP client won't connect:**
- Double-check the command path in your configuration
- Ensure `uv` is in your system PATH
- Try running `uv run doxygen-mcp` manually to test

For more help, see [BUGS.md](./BUGS.md)