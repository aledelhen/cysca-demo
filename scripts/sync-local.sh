#!/bin/sh
set -eu

branch="$(git branch --show-current)"
remote_url="$(git config --get remote.local.url || true)"

if [ -z "$branch" ]; then
    echo "No current branch detected." >&2
    exit 1
fi

if [ -z "$remote_url" ]; then
    echo "Remote 'local' is not configured." >&2
    exit 1
fi

git push "$remote_url" "HEAD:${branch}"
