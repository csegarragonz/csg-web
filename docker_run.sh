#!/bin/bash
docker run -d --name live-web -p 443:443 -p 80:80 csg-website
