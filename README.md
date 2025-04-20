# Raspberry Pi Pico projects in MicroPython

## Development environment
1. Open `mcu-pico.code-workspace` in VSCode
2. Setup common virtual environment and interpreter
    - Create virtual environment in `mcu-pico` folder using `uv sync`
    - Open any *.py file, click "select interpreter" and pick "Select at workspace level"
    - Select common interpreter from `.venv`
3. New projects (workspaces)
    - Add new workspace folder with "Add Folder to Workspace"
    - Right click added folder and select "Initialize MicroPico project"
    - Add folder name to workspace settings in `mcu-pico.code-workspace` in `micropico.additionalSyncFolders`
    - Add project to this README.md

## Running programs
### REPL
- open terminal with `MicroPico vREPL`
- type MicroPython commands or `.help`

### File
- To run single file select `Run current file on Pico`
- To upload single file select `Upload file to Pico`

### Project
- To upload project (all whitelisted files within project folder) select `Upload project to Pico`
- From drop-down list select which project to upload
- If project is missing on the list check workspace settings `micropico.additionalSyncFolders`

## Projects
Each project has it's own folder that is added to a workspace.

- Blink
- BMP280
- KY-023
