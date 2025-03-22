import os
import sys

from dotenv import load_dotenv
from PyInstaller.building.build_main import EXE, PYZ, Analysis

load_dotenv()
python_path = os.getenv("PYTHONPATH")

os.chdir(python_path)
os.environ["PYTHONPATH"] = python_path
sys.path.append(python_path)


a = Analysis(
    [os.path.join("app", "__main__.py")],
    datas=[("app", "app"), (".env", ".")],
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    name="Venv Manager",
    console=True,
    icon=["icon.ico"],
)
