# Helper script to run Doxygen MCP in Docker with the current directory mounted
$currentDir = Get-Location
$imageName = "doxygen-mcp"

Write-Host "Starting Doxygen MCP for project: $currentDir" -ForegroundColor Cyan
Write-Host "Mounted as: /app/workdir" -ForegroundColor Gray

docker run -i --rm -v "${currentDir}:/app/workdir" $imageName
