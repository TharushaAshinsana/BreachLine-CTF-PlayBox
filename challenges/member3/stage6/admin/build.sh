#!/usr/bin/env bash
set -euo pipefail

STAGE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PLAYER_DIR="$STAGE_DIR/player"

mkdir -p "$PLAYER_DIR"

gcc -std=c11 -Wall -Wextra -O0 \
    -static -fno-pie -no-pie \
    "$STAGE_DIR/admin/exfil_tool.c" \
    -o "$PLAYER_DIR/exfil_tool.elf"

strip --strip-all "$PLAYER_DIR/exfil_tool.elf"

(
    cd "$PLAYER_DIR"
    sha256sum exfil_tool.elf > exfil_tool.elf.sha256
    sha256sum -c exfil_tool.elf.sha256
)

file "$PLAYER_DIR/exfil_tool.elf"
