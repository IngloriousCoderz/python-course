# Create a virtual environment
python -m venv .venv

# Check the current paths in Python
import sys
sys.path
# ['', '/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload', '/usr/lib/python3.10/site-packages']

# Activate the virtual environment
# Windows:
.venv\Scripts\Activate.ps1 # for Powershell
.venv\Scripts\activate.bat # for Command Prompt
# Unix:
source .venv/bin/activate

# Then check again
import sys
sys.path
# ['', '/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload', '/home/iceonfire/Projects/AxL Formazione/Skylogic/python-skylogic/09-venv/.venv/lib/python3.10/site-packages']

# Installing packages

python -m pip install novas
# or
pip install novas==3.1.1.5 # optional version

# Upgrading packages

pip install --upgrade pip

# Try importing novas from global Python, then from within the venv
import novas

# Show all installed packages

pip list

# Display info about a package

pip show novas

pip freeze > requirements.txt

# Uninstalling packages

pip uninstall novas

# Installing from requirements list

pip install -r requirements.txt
