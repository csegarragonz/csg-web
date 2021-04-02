# Renew Let's Encrypt HTTPS Certificates

The website relies on HTTPS certificates released by Let's Encrypt certbot.
Every now and then we need to renew them, until this does not become a cron, the
steps to do so are:

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

