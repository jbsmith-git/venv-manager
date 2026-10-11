## Venv Manager Repo

A virtual environment manager for Python developers using Windows.

### Add to Path

To be able to rebuild a virtual environment from wherever you are:
1. Open **Edit the system environment variables** in Windows.
2. Navigate to Environment Variables > System variables > Path.
3. Add a row `C:\...\venv-manager`, wherever the repo is cloned.
4. Restart your terminal.

The virtual environment manager can now be called via the `rebuild` command.

### Usage

Call `rebuild` from a PowerShell terminal, optionally supplying a path to the project folder (default current path). This will:
1. Delete and recreate an existing virtual environment.
2. Install any packages in `requirements.txt`.
