$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$base = Join-Path $here "artifact-src\base.jpg"
$distDir = Join-Path $here "dist"
$outImg = Join-Path $distDir "planning_notes.jpg"

if (!(Test-Path $base)) {
  Write-Host "ERROR: base.jpg not found at $base"
  Write-Host "Put a JPG file as: challenges/member2/s2-planning-notes/artifact-src/base.jpg"
  exit 1
}

New-Item -ItemType Directory -Force -Path $distDir | Out-Null

# CHANGE these before final submission (must match CTFd S2 flag)
$pass = "novatech2026"
$flag = "NOVATECH{S2_PLANNING_NOTES_FLAG}"

Write-Host "[*] Building S2 builder image..."
docker build -t breachline-s2-builder $here

Write-Host "[*] Generating planning_notes.jpg..."
$cmd = "set -e; " +
       "mkdir -p /work/dist; " +
       "cp /work/artifact-src/base.jpg /work/dist/planning_notes.jpg; " +
       "printf ""NovaTech - Planning Notes\n-------------------------\nNext target: employee portal.\n\nFLAG: $flag\n"" > /work/payload.txt; " +
       "exiftool -overwrite_original -Comment=""steg-pass:$pass"" /work/dist/planning_notes.jpg >/dev/null; " +
       "steghide embed -cf /work/dist/planning_notes.jpg -ef /work/payload.txt -sf /work/dist/planning_notes.jpg -p ""$pass"" -f >/dev/null; " +
       "rm -f /work/payload.txt; " +
       "echo ""OK: built dist/planning_notes.jpg"""

docker run --rm -v "${here}:/work" breachline-s2-builder bash -lc $cmd

if (!(Test-Path $outImg)) {
  Write-Host "ERROR: Output not found: $outImg"
  exit 1
}

Write-Host "[OK] Created: $outImg"