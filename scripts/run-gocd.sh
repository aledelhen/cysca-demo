#!/bin/sh
set -eu

cleanup() {
    docker compose down -v
}

trap cleanup EXIT

docker compose up --build --abort-on-container-exit

echo "Post-run report files:"
find reports -maxdepth 4 -type f 2>/dev/null || true
