<#
.SYNOPSIS
    Health check utility for the ALMAA Discord IA platform.

.DESCRIPTION
    This script queries the state of each container defined in
    docker-compose.windows.yml and reports whether the service is
    running and, if available, its health status.  It is intended to be
    executed after the stack has been launched via install.ps1.
#>

param()

function Get-ContainerStatus {
    param([string]$Name)
    try {
        $status = docker inspect -f '{{.State.Status}}' $Name 2>$null
        $health = docker inspect -f '{{if .State.Health}}{{.State.Health.Status}}{{else}}N/A{{end}}' $Name 2>$null
        [pscustomobject]@{
            Name   = $Name
            Status = if ($status) { $status.Trim() } else { 'not_found' }
            Health = if ($health) { $health.Trim() } else { 'N/A' }
        }
    } catch {
        return [pscustomobject]@{ Name = $Name; Status = 'error'; Health = 'error' }
    }
}

$serviceNames = @(
    'almaa_nginx',
    'almaa_api',
    'almaa_redis',
    'almaa_postgres',
    'almaa_chroma',
    'almaa_minio',
    'almaa_prometheus',
    'almaa_grafana',
    'almaa_loki'
)

$results = foreach ($name in $serviceNames) {
    Get-ContainerStatus -Name $name
}

Write-Host "Container health report:" -ForegroundColor Cyan
$results | Format-Table -AutoSize