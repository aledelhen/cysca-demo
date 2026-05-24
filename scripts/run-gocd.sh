#!/bin/sh
set -eu

cleanup() {
    docker compose down -v
}

trap cleanup EXIT

export HOST_UID="$(id -u)"
export HOST_GID="$(id -g)"

docker compose up --build --abort-on-container-exit

echo "Post-run report files:"
find reports -maxdepth 4 -type f 2>/dev/null || true
