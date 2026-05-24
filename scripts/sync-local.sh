#!/bin/sh
set -eu

branch="$(git branch --show-current)"

if [ -z "$branch" ]; then
    echo "No current branch detected." >&2
    exit 1
fi

git push local "HEAD:${branch}"
