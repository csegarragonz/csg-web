# Renew Let's Encrypt HTTPS Certificates

The website relies on HTTPS certificates released by Let's Encrypt certbot.
Every now and then we need to renew them, until this does not become a cron, the
steps to do so are:

Before doing anything, SSH into the server machine and `cd ~/csg-web`.

First, stop and remove the container
```
docker stop live-web
docker rm live-web
```

Then renew the certificates:
```bash
sudo certbot renew --standalone
```

Lastly copy the key material:
```bash
sudo cp /etc/letsencrypt/live/carlossegarra.com/fullchain.pem ./keys
sudo cp /etc/letsencrypt/live/carlossegarra.com/privkey.pem ./keys
```

And re-run the container:
```bash
python3 deploy_entrypoint.py
```
