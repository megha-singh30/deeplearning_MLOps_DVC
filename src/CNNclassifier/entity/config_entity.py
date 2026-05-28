# To create custom return type, we can create our own class and use it as return type in the function.
# This is to be done inside the entity module.

# First create a dataclass (which is a constant class) for defining configuration of data ingestion.

from dataclasses import dataclass
from pathlib import Path
from CNNclassifier import *

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL : str
    local_data_file : Path
    unzip_dir : Path

@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int