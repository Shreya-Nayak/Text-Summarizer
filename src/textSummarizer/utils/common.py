#function repeatedly used so write inside utils and import from here

#using box exception

import os
from  box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

#To load any yaml files
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path to yaml file
    
    Raises:
        ValueError: if yaml file is empty
        e: empty yaml file
    
    Returns:"
        ConfigBox: ConfigBox type
    """

    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


# Creating directories

@ensure_annotations
def create_directory(path_to_directories:list, verbose=True):
    """Creates list of directory if it doesn't exist

    Args:
        path_to_directories (lsit): list of path to directory
        ignore_log(bool, optional): ignore if multiple drs is to be created. Defaults to false.
    """

    for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f" Created Directory at: {path} created successfully")


# Size of a file

@ensure_annotations
def get_size(path: Path) -> str:
    """Returns size of file in Kbytes

    Args:
        path (Path): path of file
    
    Returns:
        str: size of file in kbytes
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"
    

