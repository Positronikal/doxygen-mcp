# Doxygen MCP Server

A comprehensive Model Context Protocol (MCP) server that provides full access to Doxygen's documentation generation capabilities. This server enables AI assistants like Claude to generate, configure, and manage documentation for any supported programming language through a clean, powerful interface.

## Overview

The Doxygen MCP Server automates the generation of documentation from source code comments, parsing information about classes, functions, and variables to produce output in formats like HTML and PDF. By simplifying and standardizing the documentation process, it enhances collaboration and maintenance across diverse programming languages and project scales.

## Features

### 🚀 Core Capabilities
- **Project Management**: Initialize and configure Doxygen projects with intelligent defaults
- **Multi-Language Support**: Full support for C/C++, Python, PHP, Java, C#, JavaScript, and more
- **Documentation Generation**: Generate comprehensive documentation in multiple formats
- **Validation & Analysis**: Check documentation coverage and identify missing documentation
- **Diagram Generation**: Create UML diagrams, inheritance graphs, and call graphs
- **Configuration Management**: Advanced Doxyfile creation and management

### 📋 Supported Languages

**Primary Support:**
- C, C++, Python, PHP

**Extended Support:**
- Java, C#, JavaScript, Objective-C, Fortran, VHDL, IDL

**Additional Support (via extension mapping):**
- Batch, PowerShell, Bash, Perl, Go, and more

### 📄 Output Formats
- HTML (with interactive navigation)
- LaTeX and PDF
- XML (for further processing)
- RTF (Rich Text Format)
- Man pages
- DocBook

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
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation**
   ```bash
   python server.py --help
   ```

## Usage

### Starting the Server

```bash
# Start the MCP server
python server.py
```

The server communicates via stdin/stdout using the MCP protocol.

### Available Tools

The server provides the following tools for documentation management:

#### Project Management
- `create_doxygen_project` - Initialize a new documentation project
- `scan_project` - Analyze project structure and identify files
- `suggest_file_patterns` - Get recommendations for file inclusion patterns

#### Documentation Generation
- `generate_documentation` - Create documentation from source code
- `validate_documentation` - Check for warnings and coverage issues
- `export_documentation` - Export docs in various formats

#### Configuration
- `create_doxyfile` - Generate Doxygen configuration files
- `parse_doxyfile` - Analyze existing configurations
- `configure_project` - Modify project settings

#### Analysis & Utilities
- `analyze_coverage` - Detailed documentation coverage analysis
- `extract_api_structure` - Parse and analyze API structure
- `generate_diagrams` - Create specific diagram types
- `check_doxygen_install` - Verify system requirements

### Example Workflow

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

## File Structure

```
doxygen-mcp/
├── server.py              # Main MCP server implementation
├── requirements.txt       # Python dependencies
├── package.json           # Project metadata and configuration
├── README.md              # This documentation
├── docs/                  # Doxygen documentation (downloaded)
│   └── Doxygen/           # Official Doxygen manual
├── examples/              # Example projects and configurations
├── tests/                 # Unit tests
└── templates/             # Doxyfile templates
    ├── minimal.doxyfile
    ├── standard.doxyfile
    └── comprehensive.doxyfile
```

## Development

### Running Tests

```bash
# Install development dependencies
pip install -r requirements.txt

# Run tests
python -m pytest tests/

# Run with coverage
python -m pytest tests/ --cov=server
```

### Code Formatting

```bash
# Format code
black server.py

# Type checking
mypy server.py
```

### Adding New Features

1. **Extend DoxygenConfig**: Add new configuration options
2. **Implement Tool Handler**: Add the tool method to DoxygenServer
3. **Update Tool List**: Add tool definition to handle_list_tools
4. **Add Tests**: Create comprehensive test cases
5. **Update Documentation**: Document the new functionality

## Troubleshooting

### Common Issues

**Doxygen Not Found**
```bash
# Verify Doxygen installation
doxygen --version

# Add to PATH if needed (Windows)
set PATH=%PATH%;C:\Program Files\doxygen\bin
```

**Graphviz Diagrams Not Working**
```bash
# Test Graphviz installation
dot -V

# Install missing components
sudo apt-get install graphviz-dev  # Linux
brew install graphviz              # macOS
```

**LaTeX PDF Generation Fails**
```bash
# Test LaTeX installation
pdflatex --version

# Install missing packages
sudo apt-get install texlive-latex-extra texlive-fonts-recommended
```

**Permission Errors**
- Ensure write permissions to output directories
- Run with appropriate user privileges
- Check file system permissions

### Debug Mode

Enable detailed logging:

```bash
# Set log level to DEBUG
export PYTHONPATH=.
python -c "
import logging
logging.basicConfig(level=logging.DEBUG)
from server import main
import asyncio
asyncio.run(main())
"
```

### Performance Optimization

For large projects:
- Use `EXTRACT_ALL = NO` to reduce processing time
- Enable `OPTIMIZE_OUTPUT_FOR_C` for C projects
- Set `MAX_DOT_GRAPH_DEPTH` to limit diagram complexity
- Use `EXCLUDE_PATTERNS` to skip unnecessary files

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes with tests
4. Submit a pull request

### Guidelines
- Follow PEP 8 style guidelines
- Add comprehensive tests for new features
- Update documentation for API changes
- Ensure backward compatibility

## License

MIT License - see LICENSE file for details.

## Support

- **Issues**: Report bugs and feature requests via GitHub Issues
- **Documentation**: Full Doxygen manual included in `docs/`
- **Examples**: Sample projects in `examples/` directory

## Roadmap

### Planned Features
- [ ] Real-time documentation preview
- [ ] Integration with popular IDEs
- [ ] Custom theme support
- [ ] Advanced search capabilities
- [ ] Multi-repository documentation
- [ ] CI/CD integration helpers
- [ ] Performance analytics
- [ ] Documentation quality scoring

### Version History
- **v1.0.0**: Initial release with core functionality
- **v1.1.0**: Enhanced language support and validation
- **v1.2.0**: Advanced diagram generation
- **v2.0.0**: Complete rewrite with MCP support

---

For more information about Doxygen itself, visit [doxygen.nl](https://www.doxygen.nl/).
