from pathlib import Path
import yaml
from box import ConfigBox
from box.exceptions import BoxValueError
from movieRecommender.logging import logger
from ensure import ensure_annotations
import os


@ensure_annotations
def load_config(config_file: Path) -> ConfigBox:
        """
        Load the configuration from a YAML file and return an instance of the specified config class.
        
        Args:
            config_file (str): The name of the configuration file.
            config_class (type): The type of the configuration class to instantiate.
        
        Returns:
            any: An instance of the specified config class.
        """
        try:
            with open(config_file, "r") as file:
                config_data = yaml.safe_load(file)
                logger.info(f"Yaml file: {config_file} loaded successfully")
            return ConfigBox(config_data)
        except BoxValueError:
            raise ValueError('Yaml file is empty')
        except Exception as e:
            raise e





@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create directories at the specified paths.

    Args:
        path_to_directories (list): A list of paths where directories will be created.
        verbose (bool, optional): Whether to log information about the created directories. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

