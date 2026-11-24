# PowerShell script to run SonarScanner via Docker, loading variables from .env
# Save as scripts/run_sonar_scan.ps1

# Resolve project root (two levels up from script location)
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = Resolve-Path (Join-Path $scriptDir "..\..")

# Load .env file if present
$envFile = Join-Path $projectRoot ".env"
if (Test-Path $envFile) {
    Get-Content $envFile | ForEach-Object {
        if ($_ -match "^\s*([^#][^=]*)=(.*)$") {
            $name = $matches[1].Trim()
            $value = $matches[2].Trim()
            # Set in the current session environment
            $env:$name = $value
        }
    }
}

# Ensure required vars are set
if (-not $env:SONAR_HOST_URL) {
    Write-Error "SONAR_HOST_URL is not set. Define it in .env or as an environment variable."
    exit 1
}
if (-not $env:SONAR_TOKEN) {
    Write-Error "SONAR_TOKEN is not set. Define it in .env or as an environment variable."
    exit 1
}

# Run Docker SonarScanner
docker run --rm `
    -e SONAR_HOST_URL=$env:SONAR_HOST_URL `
    -e SONAR_TOKEN=$env:SONAR_TOKEN `
    -v "${projectRoot}:C:/usr/src" `
    -w C:/usr/src `
    sonarsource/sonar-scanner-cli
