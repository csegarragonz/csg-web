#!/bin/bash
# FIXME
#bash cv_update.sh

THIS_DIR=$(dirname -- $(readlink -f -- $0))
PROJ_ROOT="${THIS_DIR}/.."

pushd ${PROJ_ROOT} >> /dev/null

# Docker args
if [ "$1" == "--no-cache" ]; then
    NO_CACHE=$1
else
    NO_CACHE=""
fi

# Versioning
VERSION=$(< VERSION)
JEKYLL_VERSION=$(cat .env | head -1 | cut -d"=" -f2)

docker build \
    ${NO_CACHE} \
    -t csg-website:${VERSION} \
    --build-arg JEKYLL_VERSION=${JEKYLL_VERSION} \
    ${PROJ_ROOT} 

popd >> /dev/null

