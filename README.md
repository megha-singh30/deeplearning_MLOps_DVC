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
14.	First we will start with common.py file in utils folder  this stores all major functions used frequently for the project such as reading yaml, saving and loading json/binary files, reading and writing image files, creating directories during execution of the model, and getting size of an image.
a.	All these functions are declared here with decorator @ensure_annotations
A YAML or YML file with extension .yaml or .yml, has plain text in a proper structure, to store data. It is stored almost like JSON or XML but without brackets but strict indented spaces. 
There are two YAML files for the project:
1.	config.yaml file stores paths to store data, models or metadata during data ingestion, model training and testing
2.	params.yaml file stores model parameters (in this project params of model for transfer learning)
** NOW WE WILL FOLLOW THE WORKFLOW
15.	CONFIG UPDATE -- Now, updating config.yaml file to –
At this stage, config.yaml file stores details related to data ingestion like locations of the data zip file, where to download this file, where to extract the file at designated (user-defined locations) folders.

16.	ENTITY UPDATE -- For every module/stage, we have to define entiry i.e. there will be one @dataclass decorator use to define dataingestionconfiguration Class, which will provide the return type of a function (ConfigurationManager) by setting fixed datatype of each of the inputs needed by its ConfigurationManager. Therefore, for Data Ingestion stage, the inputs need are like root_dir = Path, source_URL=Path, local_data_path = Path and unzip_filepath = Path. This will be written in entity/config_entity.py
17.	CONFIGURATION MANAGER IN SRC\CONFIG -- Define, ConfigurationManager which takes the inputs from configuration and define as proper variables and create the root directory and return the configuration (it defines variables taking inputs from config file and preparing them for next stages). This we will write in config/configuration.py	
18.	COMPONENT UPDATE -- Now, we will defined the actual work of Data Ingestion Class, it will have two functions – 1) Download the data(in zip format) 2) extract the zip file. All the details needed like url, folder locations will be passed by ConfigurationManager
19.	PIPELINE UPDATE – Create a new file called “Stage01_Data_ingestion.py”. Here we will call component to process the data ingestion stage. First we will name the stage “STAGE_NAME”. make a class called DataIngestionTrainingPipeline. Define main() here and later call the main to execute dataingestion pipeline. This will help us to run it separately. It will also defined in DVC, stage by stage.
In case we do not use DVC, then we will call it from main. So we will call this pipeline from main.py() also.
AT THE END, WHEN ALL PIPELINES ARE UPDATED THEN DVC WILL BE UPDATED.

