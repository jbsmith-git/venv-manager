import sys
import os
from dotenv import load_dotenv


## Set working dir and add to sys.path
sys.path.append(os.getenv("REPO_FILEPATH"))
os.chdir(os.getenv("REPO_FILEPATH"))

## Load environment variables
load_dotenv()


from app.main_window import MainWindow


if __name__ == "__main__":

    MainWindow()
