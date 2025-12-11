import os
import yaml
from box.exceptions import BoxValueError
from box import ConfigBox
from pathlib import Path
from textSummarizer.logging import logger
from typing import Any, List, Union


def read_yaml(path_to_yaml: Union[str, Path]) -> ConfigBox:
    """Reads a YAML file and returns a ConfigBox.

    Args:
        path_to_yaml (Union[str, Path]): Path to YAML file.

    Raises:
        ValueError: If YAML file is empty.
        Exception: For other exceptions.

    Returns:
        ConfigBox: ConfigBox containing YAML contents.
    """
    try:
        with open(path_to_yaml, "r", encoding="utf-8") as yaml_file:
            content = yaml.safe_load(yaml_file)
            if content is None:
                raise ValueError(f"YAML file is empty: {path_to_yaml}")
            logger.info(f"YAML file loaded successfully: {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"YAML file is empty: {path_to_yaml}")
    except Exception as e:
        raise e


def create_directories(path_to_directories: List[Union[str, Path]], verbose: bool = True):
    """Creates a list of directories.

    Args:
        path_to_directories (List[Union[str, Path]]): List of directory paths.
        verbose (bool, optional): Whether to log creation. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


def get_size(path: Union[str, Path]) -> str:
    """Returns the size of a file in KB.

    Args:
        path (Union[str, Path]): Path to file.

    Returns:
        str: File size in KB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"
