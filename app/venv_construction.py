import os
import subprocess


def rebuild_venv(repo_name):
    cmd_filepath = os.path.join("app", "rebuild_venv.cmd")
    repos_filepath = os.path.join(os.getenv("REPOS_FILEPATH"), repo_name)

    process = subprocess.Popen(
        [cmd_filepath, repos_filepath],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        shell=True,
    )

    for line in process.stdout:
        print(line.strip())
    for line in process.stderr:
        print(line.strip())

    process.wait()
