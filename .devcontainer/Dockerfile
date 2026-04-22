FROM mcr.microsoft.com/devcontainers/python:3.10

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y \
    build-essential \
    git \
    libgl1 \
    libglib2.0-0 \
    libx11-6 \
    libxext6 \
    libxrender1 \
    libsm6 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip setuptools wheel

RUN pip install \
    numpy==1.23.5 \
    scipy==1.10.1 \
    matplotlib \
    spatialmath-python \
    roboticstoolbox-python

WORKDIR /workspace