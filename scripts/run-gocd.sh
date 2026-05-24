#!/bin/sh
set -eu

cleanup() {
    docker compose down -v
}

trap cleanup EXIT

docker compose up --build --abort-on-container-exit
