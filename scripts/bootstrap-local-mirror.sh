#!/bin/sh
set -eu

mirror_dir="${1:-/tmp/gocd-repos/demo.git}"

mkdir -p "$(dirname "$mirror_dir")"
if [ ! -d "$mirror_dir" ]; then
    git init --bare "$mirror_dir"
fi
