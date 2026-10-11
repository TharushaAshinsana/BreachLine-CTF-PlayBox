
$ErrorActionPreference = "Stop"

Write-Host "Restarting BreachLine S3 challenge..."

docker compose restart s3-web

if ($LASTEXITCODE -ne 0) {
    Write-Error "S3 challenge restart failed."
    exit 1
}

Write-Host "Checking S3 challenge status..."
docker compose ps s3-web

Write-Host "S3 challenge recovery command completed."
