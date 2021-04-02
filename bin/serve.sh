#!/bin/bash
THIS_DIR=$(dirname -- $(readlink -f -- $0))
PROJ_ROOT="${THIS_DIR}/.."

pushd ${PROJ_ROOT} >> /dev/null

docker run --rm \
    --name csg-website \
    --volume="$(PWD):/srv/jekyll" \
    -v ${KEYS_DIR}/fullchain.pem:${CLI_KEYS_DIR}
    -v ${KEYS_DIR}/privkey.pem:${CLI_KEYS_DIR}
    -p 3000:4000 \
    -it jekyll/jekyll:3.8.5 \
    jekyll serve --watch --drafts

popd >> /dev/null

