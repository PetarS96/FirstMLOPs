import os
from pathlib import Path


list_of_files = [
    ".github/workflows/.gitkeep",


#Source [ src/ ]
    "src/__init__.py",
    
    #Components
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/Model_evaluation.py",

    #Pipleines
    "src/pipeline/__init__.py",
    'src/pipeline/training_pipleline.py',
    "src/pipeline/prediction_pipeline.py"

    #
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/expection/exception.py",


#Testing 
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",

#Other
    "experiment/experiments.ipynb",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.cfg",
    "setup.py",
    "pyproject.toml",
    "tox.ini",
]


for filepath in list_of_files:
    filepath= Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok= True)
 #       logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass #create an enmpty file