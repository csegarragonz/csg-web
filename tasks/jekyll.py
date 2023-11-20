from invoke import task

from subprocess import run
from tasks.util.env import PROJ_ROOT, JEKYLL_VERSION, CONTAINER_NAME
from tasks.util.version import get_docker_tag

HOST_KEYS_DIR = "{}/keys".format(PROJ_ROOT)
CLI_KEYS_DIR = "/etc/letsencrypt/live/carlossegarra.com/"


@task
def serve(ctx):
    """
    Serve the container for development
    """
    _docker_cmd = [
        "docker run --rm",
        "--name live-web",
        "-v {}:/srv/jekyll".format(PROJ_ROOT),
        "-p 4000:4000",
        "-it jekyll/jekyll:{}".format(JEKYLL_VERSION),
        "jekyll serve --watch --drafts",
    ]
    docker_cmd = " ".join(_docker_cmd)
    print(docker_cmd)
    run(docker_cmd, shell=True, cwd=PROJ_ROOT)


@task(default=True)
def run_bg(ctx):
    """
    Run the container in dettached mode
    """
    _docker_cmd = [
        "docker run -d",
        "--name {}".format(CONTAINER_NAME),
        "-v {}/fullchain.pem:{}/fullchain.pem".format(HOST_KEYS_DIR, CLI_KEYS_DIR),
        "-v {}/privkey.pem:{}/privkey.pem".format(HOST_KEYS_DIR, CLI_KEYS_DIR),
        "-p 443:443 -p 80:80",
        get_docker_tag(),
    ]
    docker_cmd = " ".join(_docker_cmd)
    print(docker_cmd)
    run(docker_cmd, shell=True, check=True, cwd=PROJ_ROOT)
