#!/usr/bin/env sh
set -eu

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
PROJECT_ROOT="$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)"
SOURCE="$PROJECT_ROOT/skills/gauge-python-automation"
TARGET="${CODEX_HOME:-$HOME/.codex}/skills/gauge-python-automation"

mkdir -p "$(dirname -- "$TARGET")"
rm -rf "$TARGET"
cp -R "$SOURCE" "$TARGET"

printf 'Installed skill to %s\n' "$TARGET"
