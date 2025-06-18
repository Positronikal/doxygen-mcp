# Support
- **Issues**: Report bugs and feature requests via GitHub Issues
- **Documentation**: Full Doxygen manual included in `docs/`
- **Examples**: Sample projects in `examples/` directory

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