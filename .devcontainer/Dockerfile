FROM mcr.microsoft.com/devcontainers/python:3.11

RUN apt-get update && apt-get install -y --no-install-recommends \
    make git curl \
    texlive-latex-base texlive-latex-extra latexmk \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /workspaces
