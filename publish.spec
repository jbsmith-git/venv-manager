import os
import sys

from dotenv import load_dotenv
from PyInstaller.building.build_main import EXE, PYZ, Analysis

load_dotenv()
python_path = os.getenv("PYTHONPATH")

os.chdir(python_path)
os.environ["PYTHONPATH"] = python_path
sys.path.append(python_path)

REPO_FILEPATH = os.getenv("REPO_FILEPATH")

a = Analysis(
    [os.path.join(REPO_FILEPATH, "app", "__main__.py")],
    datas=[
        (os.path.join(REPO_FILEPATH, "app"), "."),
        (REPO_FILEPATH, ".env"),
    ],
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    name="Venv Manager",
    console=True,
    icon=[os.path.join(REPO_FILEPATH, "icon.ico")],
)
