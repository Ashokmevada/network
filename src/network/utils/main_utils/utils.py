import yaml
from src.network.exception.exception import NetworkSecurityException
from src.network.logging.logger import logging
import os,sys
import numpy as np
import pickle

def read_yaml_file(file_path: str) -> dict:

    try:
        # with keyowrk ensures that the file opened will be closed when the block is exited
        #safe_load() is a function from pyyaml library and it is safe then yaml.load().
        with open(file_path, "r") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    
def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:

    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path , "w") as file:
            yaml.dump(content, file)
    
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    
