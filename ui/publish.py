import datetime
import shutil
import os


class PublishApp:

    def __init__(self) -> None:
        self.app_name = "Venv Manager"
        self.repo_name = "venv-manager"
        self.packages_to_publish = {"app"}
        self.pyinstaller_options = "--noconfirm --console --onefile"
        source_filepath = os.getenv("SOURCE_FILEPATH")
        self.repo_filepath = os.path.join(source_filepath, "repos", self.repo_name)
        self.app_filepath = os.path.join(source_filepath, "apps", self.repo_name)
        self.icon_filepath = os.path.join(self.app_filepath, "app", "icon.ico")
        self.startup_filepath = os.path.join(self.app_filepath, "app", "__main__.py")
        self.archive_filepath = os.path.join(source_filepath, "apps", "archive")

    def publish(self) -> None:
        self.archive_last_publish()
        self.copy_source_files()
        self.pyinstall()
        self.remove_install_files()

    def archive_last_publish(self) -> str:
        date_code = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        if os.path.isdir(self.app_filepath):
            shutil.copytree(
                self.app_filepath,
                os.path.join(self.archive_filepath, f"{self.repo_name}-{date_code}"),
            )
            shutil.rmtree(self.app_filepath)

    def copy_source_files(self) -> None:
        for package in self.packages_to_publish:
            shutil.copytree(
                os.path.join(self.repo_filepath, package),
                os.path.join(self.app_filepath, package),
            )
            if os.path.isdir(os.path.join(self.app_filepath, package, "__pycache__")):
                shutil.rmtree(os.path.join(self.app_filepath, package, "__pycache__"))
        shutil.copy(
            os.path.join(self.repo_filepath, ".env"), os.path.join(self.app_filepath, ".env")
        )

    def pyinstall(self) -> None:
        pyinstaller_command = " ".join(
            (
                f"cd {self.app_filepath} & py -m PyInstaller {self.pyinstaller_options}",
                f"--icon {self.icon_filepath}",
                f'--name "{self.app_name}"',
                f"--add-data {self.app_filepath};.",
                self.startup_filepath,
            )
        )
        print(f"Running command:\n{pyinstaller_command}\n")
        os.system(pyinstaller_command)

    def remove_install_files(self) -> None:

        ## Copy the exe to root app dir
        exe_source = os.path.join(
            self.app_filepath,
            "dist",
            f"{self.app_name}.exe",
        )
        exe_dest = os.path.join(self.app_filepath, f"{self.app_name}.exe")
        shutil.copy(exe_source, exe_dest)

        ## Remove everything else in the dir:
        install_files = os.listdir(self.app_filepath)
        for f in install_files:
            if f in {f"{self.app_name}.exe"}:
                continue
            filepath = os.path.join(self.app_filepath, f)
            if os.path.isfile(filepath):
                os.remove(filepath)
            elif os.path.isdir(filepath):
                shutil.rmtree(filepath)


if __name__ == "__main__":

    intention = input("Publishing... Enter 'publish' to continue  ")
    if intention == "publish":
        pa = PublishApp()
        pa.publish()
    else:
        print("Publish aborted")
