from invoke import Collection

from . import cv
from . import deploy
from . import docker
from . import jekyll

ns = Collection(
    cv,
    deploy,
    docker,
    jekyll,
)
