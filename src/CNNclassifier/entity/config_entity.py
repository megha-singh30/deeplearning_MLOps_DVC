# To create custom return type, we can create our own class and use it as return type in the function.
# This is to be done inside the entity module.

# First create a dataclass (which is a constant class) for defining configuration of data ingestion.

from dataclasses import dataclass
from pathlib import Path
from src.CNNclassifier import *

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL : str
    local_data_file : Path
    unzip_dir : Path
