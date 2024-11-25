import sys
import pathlib
import os
from dotenv import load_dotenv


## Set working dir and add to sys.path
if str(pathlib.Path(__file__).resolve().parents[1]) == os.getenv("REPO_FILEPATH"):
    working_dir = os.getenv("REPO_FILEPATH")
else:
    working_dir = pathlib.Path(__file__).resolve().parents[0]
sys.path.append(working_dir)
os.chdir(working_dir)

## Load environment variables
load_dotenv()


from app.main_window import MainWindow


if __name__ == "__main__":

    MainWindow()
