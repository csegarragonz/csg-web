from invoke import task

import paramiko

from subprocess import run
from tasks.util.env import PROJ_ROOT, JEKYLL_VERSION, CONTAINER_NAME
from tasks.util.version import get_version, get_docker_tag

KEY_FILENAME = "/home/csegarra/.ssh/id_rsa"
SERVER_IP = "163.172.177.63"
SERVER_USERNAME = "csegarra"
REMOTE_DIR = "/home/{}/csg-web".format(SERVER_USERNAME)


def print_output(stream):
    for line in stream.read().splitlines():
        print(line.decode("utf-8"))


def build_push():
    build_cmd = "inv docker.build --nocache --push"
    print(build_cmd)
    run(build_cmd, shell=True, check=True, cwd=PROJ_ROOT)


@task(default=True)
def deploy(ctx):
    """
    Deploy the website on the remote server
    """
    # Build and push container
    build_push()

    # Initialize the paramiko client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=SERVER_IP, username=SERVER_USERNAME, key_filename=KEY_FILENAME)

    # Pull latest image
    dock_cmd = "docker pull {}".format(get_docker_tag())
    print("csg-paris: {}".format(dock_cmd))
    stdin, stdout, stderr = ssh.exec_command(dock_cmd)
    print_output(stdout)

    # Prepare the remote environment
    clean_cmd = "cd {} && git pull origin main && docker rm -f {}".format(REMOTE_DIR, CONTAINER_NAME)
    print("csg-paris: {}".format(clean_cmd))
    stdin, stdout, stderr = ssh.exec_command(clean_cmd)
    print_output(stdout)

    # Run remote deploy script
    run_cmd = "cd {} && python3 deploy_entrypoint.py".format(REMOTE_DIR)
    print("csg-paris: {}".format(run_cmd))
    stdin, stdout, stderr = ssh.exec_command(run_cmd)
    print_output(stdout)
    print_output(stderr)
