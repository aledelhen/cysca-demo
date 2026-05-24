#!/bin/sh
set -eu

cleanup() {
    docker compose down -v
}

trap cleanup EXIT

HOST_UID="$(id -u)" HOST_GID="$(id -g)" docker compose up --build --abort-on-container-exit
