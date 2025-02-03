#!/bin/bash

# image build script

cd "$(dirname "$0")" && set -xe

source config.sh

/bin/bash build.sh && docker run \
  --rm \
  -p 4444:4444 \
  -it \
  --platform linux/x86_64 \
  $DOCKERNAME "$@"
