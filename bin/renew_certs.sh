#!/bin/bash

##############################################################################
# sudo crontab to renew the TLS certificates used to host our personal website
#
# 0 3 1 */2 * /home/csegarra/csg-web/bin/renew_certs.sh
##############################################################################

THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]:-${(%):-%x}}" )" >/dev/null 2>&1 && pwd )"
WEB_DIR="${THIS_DIR}/.."

pushd ${WEB_DIR} >> /dev/null

# First, stop the running container
docker rm -f live-web

# Renew certificates (install certbot if it doesn't exist)
sudo certbot -q renew --standalone

# Copy keys into the web directory
KEYS_DIR=${WEB_DIR}/keys
mkdir -p ${KEYS_DIR}
sudo cp /etc/letsencrypt/live/carlossegarra.com/fullchain.pem ${KEYS_DIR}/fullchain.pem
sudo cp /etc/letsencrypt/live/carlossegarra.com/privkey.pem ${KEYS_DIR}/privkey.pem

# Give the right permissions
sudo chown -R csegarra:csegarra ${KEYS_DIR}

# Run the container again
python3 ${WEB_DIR}/deploy_entrypoint.py

popd >> /dev/null
