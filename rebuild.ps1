param(
    [string]$ProjectDirpath = $PWD.Path
)

$HostActionPreference = "Stop"
$VenvActivated = $false

try {
    # Check whether the project folder exists
    if (-Not (Test-Path $ProjectDirpath)) {
        throw "Folder $ProjectDirpath could not be found"
    }

    # Move to the project folder
    $ProjectDirpath = (Resolve-Path $ProjectDirpath).Path
    Push-Location $ProjectDirpath

    # Delete an existing virtual environment
    $VenvDirpath = Join-Path $ProjectDirpath "venv"
    if (Test-Path $VenvDirpath) {
        Write-Host "Deleting existing virtual environment..." -ForegroundColor Cyan
        Remove-Item $VenvDirpath -Recurse -Force
    }
    else {
        Write-Warning "Existing virtual environment not found"
    }

    # Create virtual environment
    Write-Host "Creating new virtual environment..." -ForegroundColor Cyan
    py -m venv venv

    # Activate virtual environment
    Write-Host "Activating virtual environment..." -ForegroundColor Cyan
    venv\Scripts\activate
    $VenvActivated = $true

    # Upgrade pip
    Write-Host "Upgrading pip..." -ForegroundColor Cyan
    py -m pip install --upgrade pip

    # Purge pip cache
    Write-Host "Purging pip cache..." -ForegroundColor Cyan
    py -m pip cache purge

    # Install packages
    $ReqsFilepath = Join-Path $ProjectDirpath "requirements.txt"
    if (Test-Path $ReqsFilepath) {
        Write-Host "Installing packages..." -ForegroundColor Cyan
        py -m pip install -r requirements.txt
        if ($LASTEXITCODE -ne 0) {
            throw "Failed to install packages"
        }
    }
    else {
        Write-Warning "requirements.txt not found"
    }

    Write-Host "Virtual environment rebuild complete" -ForegroundColor Green
}
catch {
    Write-Error $_
    exit 1
}
finally {
    Pop-Location
    if ($VenvActivated) {
        deactivate
    }
}
