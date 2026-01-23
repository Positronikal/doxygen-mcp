# docker-mcp-start.ps1
# This script starts the Doxygen MCP container for the current workspace
$projectRoot = Get-Location
$imageName = "doxygen-mcp"

Write-Host "--- Doxygen MCP Auto-Start ---" -ForegroundColor Cyan
Write-Host "Project: $projectRoot" -ForegroundColor Gray

# Check if image exists, build if missing
$image = docker images -q $imageName
if (-not $image) {
    Write-Host "Image not found. Building..." -ForegroundColor Yellow
    docker build -t $imageName .
}

# Run the container
# Note: In an IDE auto-run context, we often run in the background 
# or via the MCP client. For a 'startup script', we launch it:
docker run -i --rm -v "${projectRoot}:/app/workdir" $imageName
