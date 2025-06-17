# C++ Calculator Example

This is a sample C++ project demonstrating well-documented code that can be processed with the Doxygen MCP Server.

## Files

- `calculator.h` - Header file with class declaration and documentation
- `calculator.cpp` - Implementation of the Calculator class
- `main.cpp` - Example usage and main page documentation

## Features Demonstrated

- **Class Documentation**: Complete class with member documentation
- **Function Documentation**: Detailed parameter and return value descriptions
- **Namespace Documentation**: Organized code structure
- **Enum Documentation**: Documented enumeration types
- **Struct Documentation**: Documented data structures
- **Constants Documentation**: Mathematical constants with descriptions
- **Example Code**: Usage examples within documentation
- **Error Handling**: Documented exceptions and preconditions

## Building the Documentation

Use the Doxygen MCP Server to generate documentation:

1. Create a new Doxygen project:
   ```json
   {
     "tool": "create_doxygen_project",
     "arguments": {
       "project_name": "Calculator Example",
       "project_path": "./examples/cpp_sample",
       "language": "cpp",
       "include_subdirs": false,
       "extract_private": true
     }
   }
   ```

2. Generate the documentation:
   ```json
   {
     "tool": "generate_documentation",
     "arguments": {
       "project_path": "./examples/cpp_sample",
       "output_format": "html",
       "verbose": true
     }
   }
   ```

3. Validate the documentation:
   ```json
   {
     "tool": "validate_documentation",
     "arguments": {
       "project_path": "./examples/cpp_sample",
       "check_coverage": true,
       "warn_undocumented": true
     }
   }
   ```

## Expected Output

The generated documentation should include:

- **Main Page**: Project overview from main.cpp
- **Class List**: Calculator class with all members
- **File List**: All source files with descriptions
- **Namespace List**: MathUtils namespace
- **Class Hierarchy**: Inheritance diagrams (if applicable)
- **File Dependencies**: Include graphs
- **Function Documentation**: Detailed parameter descriptions
- **Examples**: Code examples from documentation

## Documentation Features Used

This example demonstrates the following Doxygen features:

- `@file` - File descriptions
- `@brief` - Brief descriptions
- `@param` - Parameter documentation
- `@return` - Return value documentation
- `@throw` - Exception documentation
- `@note` - Additional notes
- `@warning` - Important warnings
- `@example` - Code examples
- `@code` / `@endcode` - Code blocks
- `@namespace` - Namespace documentation
- `@class` - Class documentation
- `@struct` - Structure documentation
- `@enum` - Enumeration documentation
- `@mainpage` - Main documentation page
- `@section` - Documentation sections
- `@author` - Author information
- `@date` - Date information
- `@version` - Version information
- `@since` - Version since which feature exists
- `@pre` - Preconditions
- `@post` - Postconditions

## Compilation

To compile this example (optional):

```bash
g++ -std=c++11 -o calculator main.cpp calculator.cpp
./calculator
```

This will run the example program and demonstrate the calculator functionality.
