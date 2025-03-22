import tkinter as tk

import logic.manage_venv as mv


class MainWindow:

    def __init__(self) -> None:

        self.generate()
        self.root.mainloop()

    def generate(self) -> None:

        self.root = tk.Tk()
        self.root.title("Venv Manager")
        self.root.geometry("450x232+730+350")

        tk_args = {"font": ("Consolas", 16)}
        grid_args = {"padx": (15, 0), "pady": 10}

        repo_var = tk.StringVar()
        repo_var.set("Repository")
        tk.Entry(self.root, justify="center", textvariable=repo_var, **tk_args).grid(
            row=0, column=0, columnspan=2, **grid_args
        )

        package_var = tk.StringVar()
        package_var.set("Package")
        tk.Entry(self.root, justify="center", textvariable=package_var, **tk_args).grid(
            row=1, column=0, columnspan=2, **grid_args
        )

        tk.Button(
            self.root,
            text="Rebuild Venv",
            width=16,
            command=lambda: mv.rebuild_venv(repo_var.get()),
            **tk_args
        ).grid(row=2, column=0, sticky="W", **grid_args)

        tk.Button(
            self.root,
            text="Install Package",
            width=16,
            command=lambda: mv.install_package(repo_var.get(), package_var.get()),
            **tk_args
        ).grid(row=2, column=1, sticky="W", **grid_args)

        tk.Button(
            self.root,
            text="Install Reqs",
            width=16,
            command=lambda: mv.install_reqs(repo_var.get()),
            **tk_args
        ).grid(row=3, column=0, sticky="W", **grid_args)

        tk.Button(
            self.root,
            text="Add to Reqs",
            width=16,
            command=lambda: mv.add_to_reqs(repo_var.get(), package_var.get()),
            **tk_args
        ).grid(row=3, column=1, sticky="W", **grid_args)
