#!/bin/bash

# entrypoint

cd $(dirname $0) && set -ex

bash /opt/bin/entry_point.sh | tee selenium.log &

set +x
while true; do
  grep 'Started Selenium Standalone' selenium.log && break
done
echo 'http://localhost:4444'
set -x

exec "$@"
