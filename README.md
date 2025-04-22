# Raspberry Pi Pico projects in MicroPython

## Projects
Each project has it's own folder that is added to a workspace:
- Blink
- BMP280-SPI
- KY-023

## Development environment
1. Open `mcu-pico.code-workspace` in VSCode
1. Setup common virtual environment and interpreter
    - Create virtual environment in `mcu-pico` folder using `uv sync`
    - Open any *.py file, click "select interpreter" and pick "Select at workspace level"
    - Select common interpreter from `.venv`
1. Install MicroPico extension
1. New projects (workspaces)
    - Add new workspace folder with "Add Folder to Workspace"
    - Right click added folder and select "Initialize MicroPico project"
    - Add folder name to workspace settings in `mcu-pico.code-workspace` in `micropico.additionalSyncFolders`
    - Add `"lib"` to `python.analysis.extraPaths` in `settings.json` for VS Code to access imports from that folder
    - Add project to this README.md

## Running program
MicroPico status bar should indicate `Pico connected`

### From host
- Run single file via `Run current file on Pico` 
- Click `Run` from status bar

### From Pico
1. Upload program to Pico
    - Upload single via `Upload file to Pico`
    - Upload project (all its whitelisted files from project folder) via `Upload project to Pico`
    - If project is missing on the list check workspace settings `micropico.additionalSyncFolders`
1. Run program
    - Do "Interactive Soft Reset" via vREPL `.sr`
    - Disconnect Pico via status bar, unplug it from USB and plug back in to host USB - Pico will remain disconnected from vREPL and will execute the program
    - Plug the Pico to battery

