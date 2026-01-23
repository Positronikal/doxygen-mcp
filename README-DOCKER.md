# Running Doxygen MCP in Docker

This project can be run as a Docker container, which bundles all necessary dependencies (Python, Doxygen, Graphviz) in a consistent environment.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed on your machine.

## Building the Image

From the root of the repository, run:

```bash
docker build -t doxygen-mcp .
```

## Running the Container

Since the MCP server communicates via `stdio`, you should run it in interactive mode without a TTY for best results with some MCP clients, or simply run it as follows:

```bash
docker run -i doxygen-mcp
```

### Accessing Local Files

The MCP server has security restrictions that only allow it to access files within its current working directory (or subdirectories). To document your local code, you should mount your project directory into the container.

We recommend mounting your project to `/app/workdir`:

```bash
docker run -i \
  -v /path/to/your/project:/app/workdir \
  doxygen-mcp
```

Then, when using the tools, you can refer to your project path as `workdir`.

## Integrating with Claude Desktop

To use the Docker version with Claude Desktop, update your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "doxygen-mcp-docker": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-v",
        "/absolute/path/to/your/project:/app/workdir",
        "doxygen-mcp"
      ]
    }
  }
}
```

**Note**: Replace `/absolute/path/to/your/project` with the actual path to the code you want to document.

## Benefits of using Docker

1. **No System Dependencies**: You don't need to install Doxygen or Graphviz on your host machine.
2. **Consistent Environment**: Avoid "it works on my machine" issues.
3. **Isolation**: The MCP server only has access to the directories you explicitly mount.

