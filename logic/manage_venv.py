import subprocess
import shutil
import os


def rebuild_venv(repo):

    repo_filepath = os.path.join(os.getenv("SOURCE_FILEPATH"), "repos", repo)
    venv_filepath = os.path.join(repo_filepath, "venv")

    if os.path.isdir(venv_filepath):
        shutil.rmtree(venv_filepath)

    commands = (
        f"cd {repo_filepath}",
        "py -m venv venv",
        r"venv\Scripts\activate.bat",
        "python.exe -m pip install --upgrade pip",
        "pip cache purge",
    )
    subprocess.run(" & ".join(commands), shell=True)


def install_package(repo, package):

    repo_filepath = os.path.join(os.getenv("SOURCE_FILEPATH"), "repos", repo)
    venv_filepath = os.path.join(repo_filepath, "venv")

    if not os.path.isdir(venv_filepath):
        rebuild_venv(repo)

    commands = (
        f"cd {repo_filepath}",
        r"venv\Scripts\activate.bat",
        f"pip install {package}",
    )
    subprocess.run(" & ".join(commands), shell=True)


def install_reqs(repo):

    repo_filepath = os.path.join(os.getenv("SOURCE_FILEPATH"), "repos", repo)
    venv_filepath = os.path.join(repo_filepath, "venv")
    reqs_filepath = os.path.join(repo_filepath, "requirements.txt")

    if not os.path.isdir(venv_filepath):
        rebuild_venv(repo)

    if not os.path.isfile(reqs_filepath):
        with open(reqs_filepath, "w"):
            pass

    commands = (
        f"cd {repo_filepath}",
        r"venv\Scripts\activate.bat",
        f"pip install -r requirements.txt",
    )
    subprocess.run(" & ".join(commands), shell=True)


def add_to_reqs(repo, package):

    reqs_filepath = os.path.join(os.getenv("SOURCE_FILEPATH"), "repos", repo, "requirements.txt")

    with open(reqs_filepath, "a+") as file:
        file.write(f"\n{package}")
