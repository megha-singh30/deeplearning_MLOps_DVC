# Step by Step guide to build a deep learning model from scratch
# Step by Step guide to use basic Github commands
Implementing a deep learning with MLOps- End-to-End

Step by Step guide to build a deep learning model from scratch

## Starting a new project – CNN Classifier
1.	Create a new repository in Github
> With .gitignore, MIT license, and public
3.	Clone repository in local folder
```bash
git clone repo_link
```
4.	Create a new branch, does not commit to main branch and pull the main
```bash
git checkout -b branch_name
```
```bash
git pull origin branch_name
```
5.	Make a template.py file which contains of list of folders and some logging statements to automatically create new folders to begin the project.
6.	Do first commit-
```bash
git add .

git commit -m “Created template.py file”

git push -u main branch_name
```
7.	Run template.py file. It will create all folders listed in the file.
8.	Commit-
```bash
git add .

git commit -m “Created folder structure”

git push -u main branch_name
```
9.	Create new environment-
```bash
conda create -n cnnproject python=3.10 -y
```
(Make sure you have opened the files in Administrator mode)
10.	Activate the environment-
```bash
conda activate cnnproject
```
11.	Create requirements.txt file. Add all packages that are needed in the project. Add “– e.” at the end of file for setup.py file to read it as a package.
12.	Create setup.py file with all details like version, author details etc.
13.	Install packages-
```bash
pip install -r requirements.txt
```
14.	There is a sequence of steps to be followed for better structure preparation-
## This shows how the workflow of the project will happen, following this will make programming and structuring a lot easier.
> follow these steps for once for all modules (like data ingestion, model training, model testing) or everytime for each module
```bash
1. Update config.yaml
2. Update secrets.yaml (if we want to hide something in Github then we have login/password)
3. Update params.yaml
4. Update entity
5. Update configuration manager in src config
6. Update components
7. Update pipeline
8. Update main.py
9. Update dvc.yaml
```
14.	First we will start with common.py file in utils folder. This stores all major functions used frequently for the project such as reading yaml, saving and loading json/binary files, reading and writing image files, creating directories during execution of the model, and getting size of an image.
> Make sure to add comments (detailed) on the top of every .py file. This will help anybody who uses the code or you yourself, to know exactly what is happening in this file
a.	All these functions are declared here with decorator @ensure_annotations
16.	Now, updating config.py file to –
a.	Custom define data ingestion class to read the data url, load and save data at designated folders.

