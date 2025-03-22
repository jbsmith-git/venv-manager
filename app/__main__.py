import os
import sys

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv(".env"))
python_path = os.getenv("PYTHONPATH")

os.chdir(python_path)
os.environ["PYTHONPATH"] = python_path
sys.path.append(python_path)

from app.venv_construction import rebuild_venv

if __name__ == "__main__":
    repo_name = input("Repo name: ")
    rebuild_venv(repo_name)
