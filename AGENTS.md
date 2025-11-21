# Agent Guidelines

## Build/Test Commands
- Generate all images: `./generate_images.sh`
- Run single plot script: `python scripts/plot_<name>.py`
- Install dependencies: `pip install -r requirements.txt`

## Code Style Guidelines
- Python scripts use matplotlib and numpy imports
- Italian language for comments and print statements
- File naming: `plot_<description>.py` in scripts/ folder
- Image naming: `grafico_<description>.png` in images/ folder
- Use absolute paths when saving images
- Include print statements confirming file saves
- Virtual environment required (.venv or venv)
- Scripts should be standalone and executable

## Repository Structure
- Study materials in Italian organized by exam topics
- Scripts generate educational plots for radioamateur exam
- Images stored in images/ folder with descriptive names