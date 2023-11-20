from invoke import Collection

from . import cv
from . import deploy
from . import docker
from . import jekyll
from . import update

ns = Collection(
    cv,
    deploy,
    docker,
    jekyll,
    update,
)
