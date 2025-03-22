import os
import sys

from dotenv import load_dotenv

if os.getenv("DEBUG") == "TRUE":
    load_dotenv()
    python_path = os.getenv("PYTHONPATH")
else:
    load_dotenv(dotenv_path=os.path.join(sys._MEIPASS, ".env"))
    python_path = sys._MEIPASS

os.chdir(python_path)
os.environ["PYTHONPATH"] = python_path
sys.path.append(python_path)

from app.venv_construction import rebuild_venv

if __name__ == "__main__":
    repo_name = input("Repo name: ")
    rebuild_venv(repo_name)
