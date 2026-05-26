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

case "$remote_url" in
    file:///tmp/gocd-repos/demo.git)
        mkdir -p /tmp/gocd-repos
        if [ ! -d /tmp/gocd-repos/demo.git ]; then
            git init --bare /tmp/gocd-repos/demo.git
        fi
        ;;
esac

git push "$remote_url" "HEAD:${branch}"
