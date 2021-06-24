from invoke import task

import paramiko

from subprocess import run
from tasks.util.env import PROJ_ROOT, JEKYLL_VERSION, CONTAINER_NAME
from tasks.util.version import get_version, get_docker_tag

KEY_FILENAME = "/home/csegarra/.ssh/id_rsa"
REMOTE_DIR = "/home/carlos/csg-web"


def print_output(stream):
    for line in stream.read().splitlines():
        print(line.decode("utf-8"))


def buildPush():
    build_cmd = "inv docker.build --nocache --push"
    print(build_cmd)
    run(build_cmd, shell=True, check=True, cwd=PROJ_ROOT)


@task(default=True)
def deploy(ctx):
    """
    Deploy the remote web
    """
    # Build and push container
    buildPush()

    # Initialize the paramiko client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname="163.172.155.43", username="carlos", key_filename=KEY_FILENAME)

    # Pull latest image
    dock_cmd = "docker pull {}".format(get_docker_tag())
    print("csg-paris: {}".format(dock_cmd))
    stdin, stdout, stderr = ssh.exec_command(dock_cmd)
    print_output(stdout)

    # Stop previous docker image
    clean_cmd = "cd {} && docker rm -f {}".format(REMOTE_DIR, CONTAINER_NAME)
    print("csg-paris: {}".format(clean_cmd))
    stdin, stdout, stderr = ssh.exec_command(clean_cmd)
    print_output(stdout)

    # Rebuild docker image
    run_cmd = "cd {} && python3 deploy_entrypoint.py".format(REMOTE_DIR)
    print("csg-paris: {}".format(run_cmd))
    stdin, stdout, stderr = ssh.exec_command(run_cmd)
    print_output(stdout)
    print_output(stderr)
