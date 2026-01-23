#!/bin/bash

# Setup script for Doxygen MCP Server (Bash/Linux/WSL/Git Bash)
set -e

# Colors
CYAN='\033[0;36m'
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

print_header() {
    echo -e "\n${CYAN}============================================================${NC}"
    echo -e "${CYAN} $1${NC}"
    echo -e "${CYAN}============================================================${NC}\n"
}

print_success() { echo -e " ${GREEN}[OK]${NC} $1"; }
print_error() { echo -e " ${RED}[ERROR]${NC} $1"; }
print_warning() { echo -e " ${YELLOW}[WARN]${NC} $1"; }

print_header "Doxygen MCP Server - Setup Wizard (Bash)"

# 1. Check/Install uv
if ! command -v uv &> /dev/null; then
    print_warning "'uv' package manager not found."
    echo "Attempting to install uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    # Update current path
    export PATH="$HOME/.local/bin:$PATH"
    print_success "uv installed successfully."
else
    print_success "'uv' is already installed."
fi

# 2. Check Doxygen
if ! command -v doxygen &> /dev/null; then
    print_warning "Doxygen is not in your PATH."
    echo "It is required for generating documentation."
    echo "  - Ubuntu/Debian: sudo apt install doxygen"
    echo "  - macOS: brew install doxygen"
else
    version=$(doxygen --version)
    print_success "Doxygen found (Version: $version)"
fi

# 3. Check Graphviz
if ! command -v dot &> /dev/null; then
    print_warning "Graphviz (dot) not found."
    echo "  Required for generating diagrams."
    echo "  - Ubuntu/Debian: sudo apt install graphviz"
    echo "  - macOS: brew install graphviz"
else
    print_success "Graphviz found (dot command available)"
fi

# 4. Install Project Dependencies
print_header "Installing Python Dependencies"
if uv sync; then
    print_success "Dependencies installed successfully."
else
    print_error "Failed to sync dependencies."
    exit 1
fi

# 5. Verification
print_header "Verifying Installation"
if uv run python3 -c "import doxygen_mcp; print(doxygen_mcp.__version__)" &> /dev/null; then
    version=$(uv run python3 -c "import doxygen_mcp; print(doxygen_mcp.__version__)")
    print_success "Server Verified: doxygen-mcp v$version"
    
    echo -e "\n${GREEN}Setup Complete!${NC}\n"
    
    UV_PATH=$(command -v uv)
    PROJ_DIR=$(pwd)
    
    echo "To configure this server in your IDE:"
    echo "-----------------------------------"
    echo -e "Command: ${CYAN}$UV_PATH${NC}"
    echo -e "Args:    ${CYAN}--directory \"$PROJ_DIR\" run doxygen-mcp${NC}"
else
    print_error "Server failed to start. Try running 'uv sync' again."
    exit 1
fi
