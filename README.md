# CSG Website [![Build and Deploy](https://github.com/csegarragonz/csg-web/actions/workflows/deploy.yml/badge.svg)](https://github.com/csegarragonz/csg-web/actions/workflows/deploy.yml)

This repository holds the source code for my [personal website](
https://carlossegarra.com). The template is inspired from the [researcher](
http://ankitsultana.com/researcher) with some tweaks.

To do any changes, activate the virtual environment:

```bash
source ./bin/workon.sh

inv -l
```

then you may update any files locally, and push to GitHub. A GitHub action
should take care of propagating the updates to the live website.

## Updating Content

The main page content lives in `./index.md`. Any other page lives in the
`./pages` directory.
