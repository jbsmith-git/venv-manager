import os
import subprocess


def rebuild_venv(repo_name):
    cmd_filepath = os.path.join("logic", "rebuild_venv.cmd")
    repo_filepath = os.path.join(os.getenv("REPO_FILEPATH"), repo_name)

    process = subprocess.Popen(
        [cmd_filepath, repo_filepath],
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


if __name__ == "__main__":
    rebuild_venv("test")
