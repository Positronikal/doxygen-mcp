#!/bin/bash
# Helper script to run Doxygen MCP in Docker with the current directory mounted
CURRENT_DIR=$(pwd)
IMAGE_NAME="doxygen-mcp"

echo "Starting Doxygen MCP for project: $CURRENT_DIR"
echo "Mounted as: /app/workdir"

docker run -i --rm -v "$CURRENT_DIR:/app/workdir" $IMAGE_NAME
