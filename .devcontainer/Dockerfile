# Forza l'architettura Intel (amd64) per evitare compilazioni C++ fallite sui Mac Apple Silicon
FROM --platform=linux/amd64 mcr.microsoft.com/devcontainers/python:3.10-bookworm
# Evita messaggi di errore interattivi durante l'installazione
ENV DEBIAN_FRONTEND=noninteractive

# Installa i tool essenziali
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    gdb \
    iproute2 \
    sqlite3 \
    swig \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copia il file requirements nel container
COPY requirements.txt /tmp/pip-tmp/

# Installa le librerie Python
RUN pip3 install --upgrade pip wheel setuptools
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp

# Imposta la directory di lavoro
WORKDIR /workspace