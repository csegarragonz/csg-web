#!/bin/bash

##############################################################################
# sudo crontab to renew the TLS certificates used to host our personal website
#
# To configure, open the sudo crontab file and add the following entyr:
# sudo crontab -e
# 0 */12 * * * /home/csegarra/csg-web/bin/renew_certs.sh
##############################################################################

WEB_DIR="/home/csegarra/csg-web"

pushd ${WEB_DIR} >> /dev/null

# First, stop the running container
docker rm -f live-web

# Renew certificates (install certbot if it doesn't exist)
certbot -q renew --standalone

# Copy keys into the web directory
KEYS_DIR=${WEB_DIR}/keys
mkdir -p ${KEYS_DIR}
cp /etc/letsencrypt/live/carlossegarra.com/fullchain.pem ${KEYS_DIR}
cp /etc/letsencrypt/live/carlossegarra.com/privkey.pem ${KEYS_DIR}

# Give the right permissions
chown -R csegarra:csegarra ${KEYS_DIR}

# Run the container again
su - csegarra -c "python3 ${WEB_DIR}/deploy_entrypoint.py"

popd >> /dev/null
