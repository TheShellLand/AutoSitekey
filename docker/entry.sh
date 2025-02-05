#!/bin/bash

# entrypoint

cd $(dirname $0) && set -ex

#bash /opt/bin/entry_point.sh | tee selenium.log &
bash /opt/bin/start-xvfb.sh &

sleep 3

set +x

while true; do
  if [ ! -f selenium.log ]; then break; fi
  grep 'Started Selenium Standalone' selenium.log && break
  grep 'STARTED XVFB' selenium.log && break
done

echo 'http://localhost:4444'
set -x

exec "$@"
