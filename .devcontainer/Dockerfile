FROM mcr.microsoft.com/devcontainers/python:3.12-bookworm

# Diagram toolchain used during the Sphinx build:
#   - graphviz provides `dot` (sphinx.ext.graphviz, and PlantUML's layout engine)
#   - plantuml provides the `plantuml` wrapper and pulls in a headless JRE
# (Mermaid renders client-side in the browser, so it needs no system package.)
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        graphviz \
        plantuml \
    && rm -rf /var/lib/apt/lists/*

# Bring in uv/uvx from Astral's first-party distroless image (no third-party
# devcontainer Feature). Pinned for reproducibility.
COPY --from=ghcr.io/astral-sh/uv:0.8.19 /uv /uvx /bin/

# Version of the ubc CLI to install. Overridable at build time.
ARG UBC_VERSION=0.29.3
ENV UBC_VERSION=${UBC_VERSION}

# Install the per-platform ubc binary. The base image already provides
# git, make, curl, and the non-root `vscode` user.
COPY install-ubc.sh /tmp/install-ubc.sh
RUN chmod +x /tmp/install-ubc.sh && /tmp/install-ubc.sh "${UBC_VERSION}"
