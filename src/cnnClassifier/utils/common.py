import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
# from box import ConfigBox
from box import Box
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(file_path: str) -> Box:
    """
    Read the yaml file and return the content
    :param file_path: str: path to the yaml file
    :return: ConfigBox: ConfigBox type
    """
    try:
        with open(file_path, "r") as file:
            content = yaml.safe_load(file)
            logger.info(f"Reading the yaml file: {file_path}")
            # return ConfigBox(content)
            return Box(content)
    except BoxValueError:
        return ValueError("File empty!")
    except Exception as e:
        logger.error(f"Error in reading the yaml file: {file_path}")
        logger.error(f"Error: {e}")
        return e
    
@ensure_annotations
def create_directories(path_to_directies: list,verbose=True):
    """
    Create directories if not present
    :param path_to_directies: list: list of paths to directories
    :param verbose: bool: whether to print the message or not
    """
    for path in path_to_directies:
        if not os.path.exists(path):
            os.makedirs(path)
            if verbose:
                logger.info(f"Directory created at: {path}")
        else:
            if verbose:
                logger.info(f"Directory already exists at: {path}")             
             
             
@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save the given dictionary data as json file
    :param path: Path: path where the json file needs to be saved
    :param data: dict: data to be saved
    """
    try:
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)
        logger.info(f"Json file saved at: {path}")
    except Exception as e:
        logger.error(f"Error in saving json file: {path}")
        logger.error(f"Error: {e}")

@ensure_annotations
# def load_json(path: Path)->ConfigBox:
def load_json(path: Path)->Box:
    """
    Load the json file and return the content
    :param path: Path: path to the json file
    :return: ConfigBox: ConfigBox type
    """
    try:
        with open(path, 'r') as f:
            data = json.load(f)
        logger.info(f"Json file loaded from: {path}")
        # return ConfigBox(data)
        return Box(data)
    except Exception as e:
        logger.error(f"Error in loading json file: {path}")
        logger.error(f"Error: {e}")
        return e

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save the given data as binary file
    :param data: Any: data to be saved
    :param path: Path: path where the binary file needs to be saved
    """
    try:
        joblib.dump(value=data, filename=path)
        logger.info(f"Binary file saved at: {path}")
    except Exception as e:
        logger.error(f"Error in saving binary file: {path}")
        logger.error(f"Error: {e}")
        
@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load the binary file and return the content
    :param path: Path: path to the binary file
    :return: Any: loaded data
    """
    try:
        data = joblib.load(path)
        logger.info(f"Binary file loaded from: {path}")
        return data
    except Exception as e:
        logger.error(f"Error in loading binary file: {path}")
        logger.error(f"Error: {e}")
        return e

@ensure_annotations
def get_size(path: Path)->str:
    """
    Get the size of the file
    :param path: Path: path to the file
    :return: str: size of the file
    """
    size = round(os.path.getsize(path)/1024)
    return f"{size} KB"

def decodeImage(imgstring, filename):
    """
    Decode the base64 encoded image and save it
    :param imgstring: str: base64 encoded image
    :param filename: str: filename to save the image
    """
    imgdata = base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()
    
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, 'rb') as f:
        return base64.b64encode(f.read())
