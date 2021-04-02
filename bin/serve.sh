#!/bin/bash
THIS_DIR=$(dirname -- $(readlink -f -- $0))
PROJ_ROOT="${THIS_DIR}/.."
HOST_KEYS_DIR="${PROJ_ROOT}/keys"
CLI_KEYS_DIR="/etc/letsencrypt/live/carlossegarra.com/"

pushd ${PROJ_ROOT} >> /dev/null

# Versioning
JEKYLL_VERSION=$(cat .env | head -1 | cut -d"=" -f2)

docker run --rm \
    --name csg-website \
    --volume="$(pwd):/srv/jekyll" \
    -v ${KEYS_DIR}/fullchain.pem:${CLI_KEYS_DIR}/fullchain.pem \
    -v ${KEYS_DIR}/privkey.pem:${CLI_KEYS_DIR}/privkey.pem \
    -p 3000:4000 \
    -it jekyll/jekyll:${JEKYLL_VERSION} \
    jekyll serve --watch --drafts

popd >> /dev/null

