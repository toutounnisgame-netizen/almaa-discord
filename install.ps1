<#
.SYNOPSIS
    Installation script for the ALMAA Discord IA offline platform on
    Windows.  This script performs environment validation, prepares
    persistent storage, generates a self‑signed TLS certificate, loads
    optional pre‑bundled Docker images and boots the Docker Compose stack.

.NOTES
    - Must be executed from the project root (`almaa-discord-ia-offline`) as
      an Administrator.
    - Requires Docker Desktop with the Compose plugin and PowerShell 7+
      installed.
    - For a complete installation guide refer to docs/INSTALLATION-WINDOWS.md.
#>

param()

function Assert-Administrator {
    $identity = [Security.Principal.WindowsIdentity]::GetCurrent()
    $principal = New-Object Security.Principal.WindowsPrincipal $identity
    if (-not $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
        Write-Error "This script must be run as Administrator."
        exit 1
    }
}

function Assert-Command {
    param(
        [Parameter(Mandatory=$true)][string]$Command,
        [string]$Message
    )
    if (-not (Get-Command $Command -ErrorAction SilentlyContinue)) {
        Write-Error "$Message"
        exit 1
    }
}

function Load-EnvFile {
    param([string]$Path)
    if (-not (Test-Path $Path)) {
        Write-Error "Environment file '$Path' not found."
        exit 1
    }
    Get-Content $Path | ForEach-Object {
        $line = $_.Trim()
        if ($line -eq '' -or $line.StartsWith('#')) { return }
        $kv = $line -split '=', 2
        if ($kv.Count -eq 2) {
            $key, $value = $kv[0], $kv[1]
            # Export to current process environment
            [System.Environment]::SetEnvironmentVariable($key, $value)
        }
    }
}

function Prepare-Directories {
    $paths = @(
        'data\\postgres',
        'data\\redis',
        'data\\chroma',
        'data\\minio',
        'data\\grafana',
        'data\\prometheus',
        'certs'
    )
    foreach ($p in $paths) {
        if (-not (Test-Path $p)) {
            New-Item -ItemType Directory -Force -Path $p | Out-Null
        }
    }
}

function Generate-Certificate {
    param(
        [string]$CertDir,
        [string]$Password = 'changeit'
    )
    $certPem = Join-Path $CertDir 'cert.pem'
    $keyPem  = Join-Path $CertDir 'privkey.pem'
    if ((Test-Path $certPem) -and (Test-Path $keyPem)) {
        Write-Host "Self‑signed certificate already exists; skipping generation."
        return
    }
    Write-Host "Generating self‑signed certificate for localhost…"
    # Create certificate in the local machine store
    $cert = New-SelfSignedCertificate -DnsName "localhost" -CertStoreLocation "cert:\\LocalMachine\\My" -KeyLength 4096 -NotAfter (Get-Date).AddYears(2)
    $securePwd = ConvertTo-SecureString -String $Password -Force -AsPlainText
    $pfxPath = Join-Path $CertDir 'almaa_localhost.pfx'
    Export-PfxCertificate -Cert $cert -FilePath $pfxPath -Password $securePwd | Out-Null
    # Try to convert PFX to PEM/KEY using OpenSSL if available
    if (Get-Command openssl -ErrorAction SilentlyContinue) {
        & openssl pkcs12 -in $pfxPath -out $certPem -nokeys -nodes -password pass:$Password | Out-Null
        & openssl pkcs12 -in $pfxPath -out $keyPem  -nocerts -nodes -password pass:$Password | Out-Null
    } else {
        Write-Warning "OpenSSL not found.  Please convert '$pfxPath' to PEM and private key manually and place them in $CertDir."
    }
    # Add certificate to Trusted Root so browsers accept it without warnings
    Import-PfxCertificate -FilePath $pfxPath -Password $securePwd -CertStoreLocation "cert:\\LocalMachine\\Root" | Out-Null
    Write-Host "Certificate generation complete."
}

function Load-DockerImages {
    $tarFile = 'docker-images.tar'
    if (Test-Path $tarFile) {
        Write-Host "Loading Docker images from $tarFile…"
        docker load -i $tarFile
    } else {
        Write-Host "No docker-images.tar found.  Skipping image preload."
    }
}

function Start-Stack {
    Write-Host "Starting Docker Compose stack…"
    $composeFile = 'docker-compose.windows.yml'
    if (-not (Test-Path $composeFile)) {
        Write-Error "Compose file '$composeFile' not found."
        exit 1
    }
    docker compose -f $composeFile --env-file .env.windows up -d
    if ($LASTEXITCODE -ne 0) {
        Write-Error "docker compose up failed.  Check the output above."
        exit 1
    }
}

# -----------------------------------------------------------------------------
# Main execution
# -----------------------------------------------------------------------------

Assert-Administrator
Assert-Command -Command docker -Message "Docker CLI is not installed.  Please install Docker Desktop for Windows."
try {
    & docker compose version | Out-Null
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Docker Compose plugin is missing."
        exit 1
    }
} catch {
    Write-Error "Docker Compose plugin is missing."
    exit 1
}

# Set working directory to the location of this script
Set-Location -Path $PSScriptRoot

# Load environment variables
Load-EnvFile -Path '.env.windows'

# Prepare persistent directories
Prepare-Directories

# Generate self‑signed certificate if needed
Generate-Certificate -CertDir '.\\certs' -Password 'changeit'

# Optionally load pre‑bundled images
Load-DockerImages

# Start the stack
Start-Stack

Write-Host "Waiting for services to initialise…"
Start-Sleep -Seconds 10
docker compose ps

Write-Host "Installation complete.  Open https://localhost in your browser to access the platform." -ForegroundColor Green