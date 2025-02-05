#!/bin/bash

# image build script

cd "$(dirname "$0")" && set -xe

source config.sh

docker rm -f $DOCKERNAME || echo DELETED

/bin/bash build.sh && \
docker run \
  --rm \
  --platform linux/x86_64 \
  -p 4444:4444 \
  --name $DOCKERNAME \
  $DOCKERNAME \
  pytest --log-cli-level error "$@"
