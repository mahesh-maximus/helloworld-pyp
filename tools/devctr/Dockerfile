# FROM ubuntu:latest
FROM ubuntu:20.04

ARG PF_SRC_DIR="/hwpyp"
ARG TINI_VERSION_TAG="v0.18.0"
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get -y install --no-install-recommends \
        binutils-dev \
        git \
        curl \
        tar \
        python \
        python3 \
        python3-dev \
        python3-pip \
        python3-venv \
        && python3 -m pip install \
            watchdog \
            setuptools \
            wheel \
            build \
            twine \
            helloworld-pyp \
        && python3 -m pip install --upgrade pip

# Add the tini init binary.
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION_TAG}/tini-static-amd64 /sbin/tini
RUN chmod +x /sbin/tini

WORKDIR "$PF_SRC_DIR"
ENTRYPOINT ["/sbin/tini", "--"]
