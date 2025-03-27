import os
from pathlib import Path
import logging

project_name = "wine-e2e-project"
logging.basicConfig(level = logging.INFO,
                    format  ='[%(asctime)s]: %(message)s:')

list_of_files = [
    ".github/workflows/.gitkeep"
    f"src/{project_name}/__init__.py", # Create the constructor for import files as packages
    f"src/{project_name}/components/__init__.py", # Data code
    f"src/{project_name}/utils/__init__.py", # Generic functionalities to define
    f"src/{project_name}/utils/common.py", # Generic functions file
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py", # Data pipelines code
    f"src/{project_name}/entity/__init__.py", 
    f"src/{project_name}/entity/config_entity.py", # Configuration details
    f"src/{project_name}/constants/__init__.py", # To define some constants
    "config/config.yaml", # Configuration details for the ML models
    "params.yaml", # Parameters for the ML model
    "schema.yaml",
    "main.py",
    "Dockerfile",
    # "requierements.txt",
    "setup.py", # Use to create the entire project as a package
    "research/research.ipynb",
    "templates/index.html",
    "templates/results.html"
]

# Loop tp create all fthe dirs and files above
for filepath in list_of_files:
    filepath = Path(filepath)
    file_dir, file_name = os.path.split(filepath)
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory {file_dir} for the file: {file_name}")
    
    elif (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file {filepath}")
        
    else:
        logging.info(f"{file_name} already exist")