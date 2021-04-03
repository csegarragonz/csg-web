from invoke import task

from os.path import exists
from subprocess import run
from shutil import copyfile, rmtree
from tasks.util.env import PROJ_ROOT

CV_DIR = "{}/{}".format(PROJ_ROOT, "CV")
ASSETS_DIR = "{}/{}".format(PROJ_ROOT, "assets")

# Repo's CV information
FILE_NAME = "SegarraCarlos_CV"
REPO_NAME = "csg-projects/csg-cv"
REPO_DIR = "short-w-images"
DOCKER_IMAGE = "moss/xelatex"
LATEX_CMD = "xelatex"


@task(default=True)
def update(ctx):
    """
    Update CV in current repository
    """
    # Clean up beforehand
    try:
        rmtree(CV_DIR)
    except FileNotFoundError:
        pass

    # Clone repository
    git_cmd = "git clone git@github.com:{}.git {}".format(REPO_NAME, CV_DIR)
    print(git_cmd)
    run(git_cmd, shell=True, cwd=PROJ_ROOT, check=True)

    # Compile the CV
    _docker_cmd = [
        "docker run --rm",
        "-v {}/{}:/work".format(CV_DIR, REPO_DIR),
        "--user 1000:1000",
        "-w /work",
        "{} {}".format(DOCKER_IMAGE, LATEX_CMD),
        "{}.tex".format(FILE_NAME),
    ]
    docker_cmd = " ".join(_docker_cmd)
    print(docker_cmd)
    run(docker_cmd, shell=True, cwd=PROJ_ROOT, check=True)

    # Copy the file and remove cleanup
    src_path = "{}/{}/{}.pdf".format(CV_DIR, REPO_DIR, FILE_NAME)
    dst_path = "{}/{}.pdf".format(ASSETS_DIR, FILE_NAME)
    copyfile(src_path, dst_path)
    rmtree(CV_DIR)
