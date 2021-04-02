#!/bin/bash

THIS_DIR=$(dirname -- $(readlink -f -- $0))
PROJ_ROOT="${THIS_DIR}/.."
HOST_KEYS_DIR="${PROJ_ROOT}/keys"
CLI_KEYS_DIR="/etc/letsencrypt/live/carlossegarra.com/"

pushd ${PROJ_ROOT} >> /dev/null

# Versioning
VERSION=$(< VERSION)

docker run -d \
    --name live-web \
    -v ${KEYS_DIR}/fullchain.pem:${CLI_KEYS_DIR}
    -v ${KEYS_DIR}/privkey.pem:${CLI_KEYS_DIR}
    -p 443:443 -p 80:80 \
    csg-website:${VERSION}

popd >> /dev/null

