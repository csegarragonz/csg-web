from datetime import datetime
from invoke import task
from os.path import join
from subprocess import run
from tasks.util.env import PROJ_ROOT


@task
def last_modified(ctx):
    """
    Update the last-modified entry in the footer
    """
    current_date = datetime.now().strftime("%d\\/%m\\/%Y")
    config_file = join(PROJ_ROOT, "_config.yml")
    sed_cmd = "sed -i "
    sed_cmd += "'s/^footer_text: \"Last update: .*$"
    sed_cmd += "/footer_text: \"Last update: {}\"/g'".format(current_date)
    sed_cmd += " {}".format(config_file)
    print(sed_cmd)
    run(sed_cmd, shell=True, check=True)
