#!/usr/bin/env sh
set -eu

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
PROJECT_ROOT="$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)"
SOURCE="$PROJECT_ROOT/skills/cysca-qa-complex-systems"
TARGET="${CODEX_HOME:-$HOME/.codex}/skills/cysca-qa-complex-systems"

mkdir -p "$(dirname -- "$TARGET")"
rm -rf "$TARGET"
cp -R "$SOURCE" "$TARGET"

printf 'Installed skill to %s\n' "$TARGET"
