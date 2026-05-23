FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl gnupg ca-certificates unzip nodejs npm \
    && rm -rf /var/lib/apt/lists/*

RUN npm install -g @getgauge/cli

WORKDIR /app

COPY requirements.txt .
RUN python -m venv /app/.venv \
    && /app/.venv/bin/pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["sh", "-c", "export GAUGE_PYTHON_COMMAND=${GAUGE_PYTHON_COMMAND:-/app/.venv/bin/python} && exec gauge run specs"]
