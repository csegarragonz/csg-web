from invoke import task

from subprocess import run
from tasks.util.env import PROJ_ROOT, JEKYLL_VERSION
from tasks.util.version import get_version, get_docker_tag


@task(default=True)
def build(ctx, nocache=False, push=False):
    """
    Build the docker image
    """
    # First update the CV
    cv_cmd = "inv cv"
    print(cv_cmd)
    run(cv_cmd, shell=True, cwd=PROJ_ROOT, check=True)

    if nocache:
        no_cache_str = "--no-cache"
    else:
        no_cache_str = ""

    # Then build the image
    _docker_cmd = [
        "docker build",
        no_cache_str,
        "-t {}".format(get_docker_tag()),
        "--build-arg JEKYLL_VERSION={}".format(JEKYLL_VERSION),
        PROJ_ROOT,
    ]
    docker_cmd = " ".join(_docker_cmd)
    print(docker_cmd)
    run(docker_cmd, shell=True, check=True, cwd=PROJ_ROOT, env={"DOCKER_BUILDKIT": "1"})

    # Push if necessary
    if push:
        push_cmd = "docker push {}".format(get_docker_tag())
        print(push_cmd)
        run(push_cmd, shell=True, check=True, cwd=PROJ_ROOT)
