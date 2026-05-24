#!/bin/sh
set -eu

mkdir -p /home/go/.gauge/config /home/go/.gauge/plugins /home/go/.gauge/logs
mkdir -p /workspace/reports /workspace/logs
chown -R 997:984 /home/go /workspace

export HOME=/home/go
export PYTHONPATH=/workspace
export GAUGE_PYTHON_COMMAND="${GAUGE_PYTHON_COMMAND:-/app/.venv/bin/python}"

cd /workspace
exec gauge run specs --env docker --log-level debug
