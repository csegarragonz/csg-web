from invoke import task
from os.path import join
from subprocess import run
from shutil import copyfile, rmtree
from tasks.util.env import PROJ_ROOT

CV_DIR = "{}/{}".format(PROJ_ROOT, "CV")
ASSETS_DIR = "{}/{}".format(PROJ_ROOT, "assets")

# Repo's CV information
FILE_NAME = "SegarraCarlos_CV"
REPO_NAME = "csegarragonz/csg-cv"
REPO_DIR = "academic"


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
    git_cmd = "git clone https://github.com/{}.git {}".format(REPO_NAME, CV_DIR)
    print(git_cmd)
    run(git_cmd, shell=True, cwd=PROJ_ROOT, check=True)

    # Compile the CV
    academic_cv_dir = join(CV_DIR, REPO_DIR)
    run("make", shell=True, cwd=academic_cv_dir, check=True)

    # Copy the file and remove cleanup
    src_path = join(academic_cv_dir, f"{FILE_NAME}.pdf")
    dst_path = "{}/{}.pdf".format(ASSETS_DIR, FILE_NAME)
    copyfile(src_path, dst_path)
    rmtree(CV_DIR)
