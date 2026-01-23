<#
.SYNOPSIS
    Setup script for Doxygen MCP Server
    Automates dependency installation, configuration, and environment verification.
#>

$ErrorActionPreference = "Stop"

function Print-Header {
    param([string]$Title)
    Write-Host ""
    Write-Host "============================================================" -ForegroundColor Cyan
    Write-Host " $Title" -ForegroundColor Cyan
    Write-Host "============================================================" -ForegroundColor Cyan
    Write-Host ""
}

function Print-Success {
    param([string]$Message)
    Write-Host " [OK] $Message" -ForegroundColor Green
}

function Print-Error {
    param([string]$Message)
    Write-Host " [ERROR] $Message" -ForegroundColor Red
}

function Print-Warning {
    param([string]$Message)
    Write-Host " [WARN] $Message" -ForegroundColor Yellow
}

function Check-Command {
    param([string]$Command)
    return (Get-Command $Command -ErrorAction SilentlyContinue)
}

function Add-To-Session-Path {
    param([string]$PathToAdd)
    if (Test-Path $PathToAdd) {
        if ($env:PATH -notlike "*$PathToAdd*") {
            $env:PATH = "$PathToAdd;$env:PATH"
            Write-Host "Temporarily added to PATH: $PathToAdd" -ForegroundColor Gray
            return $true
        }
    }
    return $false
}

Print-Header "Doxygen MCP Server - Setup Wizard"

# -----------------------------------------------------------------------------
# 1. UV Package Manager
# -----------------------------------------------------------------------------
# Check if installed
if (-not (Check-Command "uv")) {
    # Check default install location
    $uvLocalPath = "$HOME\.local\bin"
    if (Test-Path "$uvLocalPath\uv.exe") {
        Add-To-Session-Path $uvLocalPath | Out-Null
    }
}

if (-not (Check-Command "uv")) {
    Print-Warning "'uv' package manager not found."
    Write-Host "Attempting to install uv..." -ForegroundColor Gray
    try {
        irm https://astral.sh/uv/install.ps1 | iex
        Add-To-Session-Path "$HOME\.local\bin" | Out-Null
        Print-Success "uv installed successfully."
    }
    catch {
        Print-Error "Failed to install uv. Please install manually: https://docs.astral.sh/uv/"
        exit 1
    }
} else {
    Print-Success "'uv' is installed."
}

# -----------------------------------------------------------------------------
# 2. Doxygen
# -----------------------------------------------------------------------------
# Check default location if not in path
if (-not (Check-Command "doxygen")) {
    Add-To-Session-Path "C:\Program Files\doxygen\bin" | Out-Null
}

if (-not (Check-Command "doxygen")) {
    Print-Warning "Doxygen not found."
    Write-Host "Attempting to install via winget..." -ForegroundColor Gray
    try {
        winget install -e --id DimitriVanHeesch.Doxygen --accept-source-agreements --accept-package-agreements
        # Refresh path attempt
        Add-To-Session-Path "C:\Program Files\doxygen\bin" | Out-Null
    }
    catch {
        Print-Error "Failed to install Doxygen automatically."
        Write-Host "Please download from: https://www.doxygen.nl/download.html"
    }
}

if (Check-Command "doxygen") {
    try {
        $ver = (doxygen --version 2>&1) | Out-String
        Print-Success "Doxygen found (Version: $($ver.Trim()))"
    } catch {
        Print-Warning "Doxygen found but failed to report version."
    }
} else {
    Print-Error "Doxygen is still missing. Documentation generation will fail."
}

# -----------------------------------------------------------------------------
# 3. Graphviz
# -----------------------------------------------------------------------------
# Check default location if not in path
if (-not (Check-Command "dot")) {
    Add-To-Session-Path "C:\Program Files\Graphviz\bin" | Out-Null
}

if (-not (Check-Command "dot")) {
    Print-Warning "Graphviz (dot) not found."
    Write-Host "Attempting to install via winget..." -ForegroundColor Gray
    try {
        winget install -e --id Graphviz.Graphviz --accept-source-agreements --accept-package-agreements
        # Refresh path attempt
        Add-To-Session-Path "C:\Program Files\Graphviz\bin" | Out-Null
    }
    catch {
        Print-Error "Failed to install Graphviz automatically."
        Write-Host "Please download from: https://graphviz.org/download/"
    }
}

if (Check-Command "dot") {
    Print-Success "Graphviz found (dot command available)"
} else {
    Print-Warning "Graphviz missing. Diagrams will not be generated."
}

# -----------------------------------------------------------------------------
# 4. Install Project Dependencies
# -----------------------------------------------------------------------------
Print-Header "Installing Python Dependencies"
try {
    Write-Host "Running 'uv sync'..." -ForegroundColor Gray
    uv sync
    Print-Success "Dependencies installed successfully."
}
catch {
    Print-Error "Failed to sync dependencies. Check your internet connection."
    exit 1
}

# -----------------------------------------------------------------------------
# 5. Verification
# -----------------------------------------------------------------------------
Print-Header "Verifying Installation"
try {
    # Check version using python module to avoid path issues during first install
    $version = uv run python -c "import doxygen_mcp; print(doxygen_mcp.__version__)"
    Print-Success "Server Verified: doxygen-mcp v$version"
    
    Write-Host ""
    Write-Host "Setup Complete!" -ForegroundColor Green
    Write-Host ""
    
    $uvPath = (Get-Command uv).Source
    $projectDir = $PWD.Path
    
    # Check if we need to warn about PATH
    $pathModified = $false
    if ($env:PATH -like "*$HOME\.local\bin*") { $pathModified = $true }
    if ($env:PATH -like "*doxygen*") { $pathModified = $true }
    
    Write-Host "To configure this server in your IDE:"
    Write-Host "-----------------------------------"
    Write-Host "Command: $uvPath" -ForegroundColor Magenta
    Write-Host "Args:    --directory `"$projectDir`" run doxygen-mcp" -ForegroundColor Magenta
    
    Write-Host ""
    Write-Host "IMPORTANT:" -ForegroundColor Yellow
    Write-Host "If you just installed tools, you may need to restart your shell/IDE" -ForegroundColor Yellow
    Write-Host "or add the following to your system PATH:" -ForegroundColor Yellow
    Write-Host " - C:\Program Files\doxygen\bin"
    Write-Host " - C:\Program Files\Graphviz\bin"
    Write-Host " - $HOME\.local\bin"
}
catch {
    Print-Error "Server failed to start."
    exit 1
}