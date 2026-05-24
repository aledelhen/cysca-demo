#!/bin/sh
set -eu

printf 'GoCD preflight: pwd=%s\n' "$(pwd)"
git rev-parse --short HEAD
ls -ld specs scripts docker-compose.yml

cleanup() {
    docker compose down -v
}

trap cleanup EXIT

docker compose up --build --abort-on-container-exit
