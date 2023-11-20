from subprocess import run
from os.path import dirname, realpath

PROJ_ROOT = dirname(dirname(dirname(realpath(__file__))))
HOST_KEYS_DIR = "{}/keys".format(PROJ_ROOT)
CLI_KEYS_DIR = "/etc/letsencrypt/live/carlossegarra.com/"
WEB_CTR_NAME = "live-web"


def get_docker_tag():
    with open("VERSION", "r") as fh:
        ver = fh.read()
        ver = ver.strip()

    return "csegarragonz/csg-website:{}".format(ver)


def run_bg_invokeless():
    """
    Run the container in dettached mode
    """
    _docker_cmd = [
        "docker run -d",
        "--name {}".format(WEB_CTR_NAME),
        "-v {}/fullchain.pem:{}/fullchain.pem".format(HOST_KEYS_DIR, CLI_KEYS_DIR),
        "-v {}/privkey.pem:{}/privkey.pem".format(HOST_KEYS_DIR, CLI_KEYS_DIR),
        "-p 443:443 -p 80:80",
        get_docker_tag(),
    ]
    docker_cmd = " ".join(_docker_cmd)
    print(docker_cmd)
    run(docker_cmd, shell=True, check=True, cwd=PROJ_ROOT)


if __name__ == "__main__":
    run_bg_invokeless()
