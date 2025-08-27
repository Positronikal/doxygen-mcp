# Development

## Running Tests
```bash
# Install development dependencies
pip install -r requirements.txt

# Run tests
python -m pytest tests/

# Run with coverage
python -m pytest tests/ --cov=server
```

## Code Formatting
```bash
# Format code
black server.py

# Type checking
mypy server.py
```

## Performance Optimization
For large projects:
- Use `EXTRACT_ALL = NO` to reduce processing time
- Enable `OPTIMIZE_OUTPUT_FOR_C` for C projects
- Set `MAX_DOT_GRAPH_DEPTH` to limit diagram complexity
- Use `EXCLUDE_PATTERNS` to skip unnecessary files

## Adding New Features
1. **Extend DoxygenConfig**: Add new configuration options
2. **Implement Tool Handler**: Add the tool method to DoxygenServer
3. **Update Tool List**: Add tool definition to handle_list_tools
4. **Add Tests**: Create comprehensive test cases
5. **Update Documentation**: Document the new functionality
