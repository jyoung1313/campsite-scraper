# Project Setup (Windows)
Install python (ensure to check "Add python.exe to PATH"):

Install uv:
`powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

Setup virtual environment and running project:
`uv venv --python 3.13`
`source .venv/Srcipts/activate`
`uv sync`
`uv run main.py`

Add a dependency (while in activated venv):
`uv pip install <dependency_name>`

# Importing project into vscode
Install Python extension in vscode.
Setup interpreter:
`(Ctrl+Shift+P) -> Search for "Python: Select Interpreter"`
`Select the virutal environment that you created.`
Setup test environment:
`(Ctrl+Shift+P) -> Search for "Python: Configure Tests"`
`Select "pytest"`
`Select the "tests" directory`