import os
from box.exceptions import BoxValueError
import yaml
from CNNclassifier import logger
import json
import joblib
import numpy as np
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

# Common utility functions for the CNN classifier project:
# 1. read_yaml: Reads a YAML file and returns its contents as a ConfigBox object.
# 2. save_json: Saves data to a JSON file.
# 3. load_json: Loads data from a JSON file.
# 4. save_bin: Saves data to a binary file using joblib.
# 5. load_bin: Loads data from a binary file using joblib.
# 6. encode_image_to_base64: Encodes an image to a base64 string.
# 7. decode_base64_to_image: Decodes a base64 string back to an image and saves it to the specified path.
# 8. get_size: Gets the size of an image in bytes.
# 9. create_directories: Creates directories if they do not exist.
# These functions are decorated with @ensure_annotations to ensure that they are called with the correct arguments. 
# This helps to catch errors early and makes the code more robust. 
# The logger is used to log important information and errors throughout the functions, which can be helpful for debugging and monitoring the application.

@ensure_annotations
def read_yaml(path_to_yaml) -> ConfigBox:
    """
    Reads a YAML file and returns its contents as a ConfigBox object.

    Args:
        path_to_yaml (Path): The path to the YAML file. 
    Returns:
        ConfigBox: The contents of the YAML file as a ConfigBox object. 
    Raises:
        BoxValueError: If the YAML file is empty or cannot be parsed.       
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        logger.error(f"Error parsing YAML file: {e}")
        raise
    except Exception as e:
        logger.error(f"Error reading YAML file: {e}")
        raise

@ensure_annotations
def save_json(path: Path, data: dict) -> None:
    """
    Saves data to a JSON file.

    Args:
        path (Path): The path to the JSON file.
        data (dict): The data to be saved to the JSON file.
    Returns:
        None
    Raises:
        Exception: If there is an error saving the JSON file.
    """
    try:
        with open(path, "w") as json_file:
            json.dump(data, json_file, indent=4)
            logger.info(f"Data successfully saved to {path}")
    except Exception as e:
        logger.error(f"Error saving JSON file: {e}")
        raise


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads data from a JSON file.

    Args:
        path (Path): The path to the JSON file.
    Returns:
        ConfigBox: The data loaded from the JSON file.
    Raises:
        Exception: If there is an error loading the JSON file.
    """
    try:
        with open(path, "r") as json_file:
            data = json.load(json_file)
            logger.info(f"Data successfully loaded from {path}")
            return ConfigBox(data)
    except Exception as e:
        logger.error(f"Error loading JSON file: {e}")
        raise
    

@ensure_annotations
def save_bin(data: Any, path: Path) -> None:
    """
    Saves data to a binary file using joblib.

    Args:
        data (Any): The data to be saved to the binary file.
        path (Path): The path to the binary file.
    Returns:
        None
    Raises:
        Exception: If there is an error saving the binary file.
    """
    try:
        joblib.dump(data, path)
        logger.info(f"Data successfully saved to {path}")
    except Exception as e:
        logger.error(f"Error saving binary file: {e}")
        raise

@ensure_annotations
def load_bin(path: Path) -> ConfigBox:
    """Loads data from a binary file using joblib.
    Args:
        path (Path): The path to the binary file.
    Returns:
        ConfigBox: The data loaded from the binary file.
    Raises:
        Exception: If there is an error loading the binary file.
    """
    try:
        data = joblib.load(path)
        logger.info(f"Data successfully loaded from {path}")
        return ConfigBox(data)
    except Exception as e:
        logger.error(f"Error loading binary file: {e}")
        raise

@ensure_annotations
def encode_image_to_base64(cropped_image_path: Path) -> str:
    """
    Encodes an image to a base64 string.

    Args:
        cropped_image_path (Path): The path to the cropped image file.
    Returns:
        str: The base64 encoded string of the image.
    Raises:
        Exception: If there is an error encoding the image.
    """
    try:
        with open(cropped_image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            logger.info(f"Image successfully encoded to base64 from {cropped_image_path}")
            return encoded_string
    except Exception as e:
        logger.error(f"Error encoding image to base64: {e}")
        raise

@ensure_annotations
def decode_base64_to_image(encoded_string: str, output_image_path: Path) -> None:
    """Decodes a base64 string back to an image and saves it to the specified path.     
    Args:
        encoded_string (str): The base64 encoded string of the image.
        output_image_path (Path): The path where the decoded image will be saved.
    Returns:
        None
    Raises:
        Exception: If there is an error decoding the image.
    """
    try:
        with open(output_image_path, "wb") as image_file:
            image_file.write(base64.b64decode(encoded_string))
            logger.info(f"Image successfully decoded from base64 and saved to {output_image_path}")
    except Exception as e:
        logger.error(f"Error decoding base64 to image: {e}")
        raise

@ensure_annotations
def get_size(image_path: Path)-> str:
    """Gets the size of an image in bytes.
    Args:
        image_path (Path): The path to the image file.
    Returns:
        str: The size of the image in kilobytes.
    Raises:
        Exception: If there is an error getting the size of the image.
    """
    try:
        size_in_kB = os.path.getsize(image_path) / 1024
        logger.info(f"Size of the image at {image_path} is {size_in_kB:.2f} kB")   
        return f"~ {size_in_kB:.2f} kB"
    except Exception as e:
        logger.error(f"Error getting size of the image: {e}")
        raise

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True) -> None:
    """
    Creates directories if they do not exist.

    Args:
        path_to_directories (list): A list of paths to the directories to be created.
        verbose (bool, optional): If True, logs the creation of each directory. Defaults to True.
    Returns:
        None
    Raises:
        Exception: If there is an error creating the directories.
    """
    try:
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Directory created at: {path}")
    except Exception as e:
        logger.error(f"Error creating directories: {e}")
        raise
        