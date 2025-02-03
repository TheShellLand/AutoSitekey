#!/bin/bash

# image build script

cd "$(dirname "$0")" && set -xe

source config.sh

/bin/bash build.sh && \
docker run \
  --rm \
  --platform linux/x86_64 \
  -p 4444:4444 \
  $DOCKERNAME \
  pytest "$@"
