# Salary-Linear-Regression-
Simple Linear Regression implementation on salaries dataset from Kaggle (Demo). 


## Notes
- Make sure you download Python, any version is fine, 3.14.x ideally.
- VSCode needs to be downloaded as well.


## Instructions to creating a Virtual Environment (always start here)
- Purpose: To make sure you keep your python package installs (which you will be using when creating ml projects, separate from your actual machine)
- Step 1: Open up new terminal by going to top banner to `terminal` -> `New Terminal`
- Step 2: Make sure that if you type in `ls`, you see requirements.txt, that's how you know you're in the right file path.
- Step 2: type in terminal `python -m venv VirtualEnv`
- Step 3: If you don't have one, create a .gitignore, and insert `/VirtualEnv` so you're not committing your virtual environment to your repository.
- Type in `VirtualEnv/Scripts/Activate`
- Now you're in a Virtual Environment


## PIP installs
- These are python packages that use pip as the install engine.
- In the case where you run a python script and it says a package isn't found type in `pip install **package_name**` MAKE SURE that the virtual environment is turned on first, refer to the instructions above.
- In case you're unsure about all the packages you installed using `pip` type in `pip freeze > requirements.txt`, this will put all the python dependencies into a single file, which if you ever get a new environment, you can redownload all the packages with `pip install -r requirements.txt`