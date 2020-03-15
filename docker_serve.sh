#!/bin/bash
docker run --rm --name csg-website --volume="$PWD:/srv/jekyll" -p 3000:4000 -it jekyll/jekyll:3.8.5 jekyll serve --watch --drafts
