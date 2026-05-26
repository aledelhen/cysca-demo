#!/bin/sh
set -eu

cleanup() {
    docker compose down -v
}

trap cleanup EXIT

export HOST_UID="$(id -u)"
export HOST_GID="$(id -g)"

./scripts/bootstrap-local-mirror.sh

mkdir -p reports logs
docker compose up --build --abort-on-container-exit

echo "Post-run report files:"
find reports -maxdepth 4 -type f 2>/dev/null || true
echo "Post-run report dir:"
ls -ld reports reports/html-report reports/xml-report 2>/dev/null || true
