'''
How to restore dataset upon deletion.

-- Make sure you have already started virtual environment at this point...

1) Open the terminal, this can be done by pressing terminal in the top banner menu and selecting 'new terminal'
2) Type 'ls' and hit enter
        - You should see an entry that says scripts
3) Type 'cd scripts' and hit enter
        -  Type in 'ls' again and ensure data_restore.py exists.
4) Type 'python data_restore.py' and hit enter


- In the case it says kagglehub isn't installed.
            - type 'python -m venv VirtualEnv' and hit enter
            - type 'VirtualEnv/Scripts/Activate' and hit enter
            - type 'pip install kagglehub' and hit enter
            - repeat step 4.
'''

import kagglehub
import time 
import os
import shutil


# Make sure you choose a dataset, that has at least 1000 rows, ideally ~15 columns.
# replace Salary_dataset.csv with the name of the csv file 
# https://www.kaggle.com/datasets/abhishek14398/salary-dataset-simple-linear-regression?select=Salary_dataset.csv

def create_file_paths(file_path):
        return os.path.join(file_path, 'Salary_dataset.csv')

def drop_source_path(file_path):
    kaggle_filepath_str = ""

    for file_element in file_path.split('\\')[:4]:
        kaggle_filepath_str += file_element + '\\'
    
    kaggle_filepath_str += 'kagglehub'
    return kaggle_filepath_str

# Take the file path of from the kaggle website up until the question mark and after the datasets/ part of the url
# https://www.kaggle.com/datasets/abhishek14398/salary-dataset-simple-linear-regression?select=Salary_dataset.csv
# /abhishek14398/salary-dataset-simple-linear-regression

dataset = kagglehub.dataset_download("abhishek14398/salary-dataset-simple-linear-regression")

source_filepath = create_file_paths(dataset)
dest_filepath = create_file_paths(os.path.join(os.path.dirname(os.getcwd()),'data'))

try:
    shutil.copy(source_filepath, dest_filepath)
    shutil.rmtree(drop_source_path(source_filepath))
except FileExistsError as e:
    print("File already exists in directory")
