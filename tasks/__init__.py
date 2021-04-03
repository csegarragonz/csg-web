from invoke import Collection

from . import cv
from . import docker
from . import jekyll

ns = Collection(
    cv,
    docker,
    jekyll,
)
