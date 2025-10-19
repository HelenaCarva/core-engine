import logging
import os
from typing import Any, Dict, List, Optional

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def load_config(file_path: str) -> Dict[str, Any]:
    config = {}
    try:
        with open(file_path, 'r') as file:
            config = eval(file.read())
    except FileNotFoundError:
        logging.error(f"Config file not found at {file_path}")
    except Exception as e:
        logging.error(f"Error loading config: {str(e)}")
    return config

def save_config(file_path: str, config: Dict[str, Any]) -> None:
    try:
        with open(file_path, 'w') as file:
            file.write(str(config))
    except Exception as e:
        logging.error(f"Error saving config: {str(e)}")

def get_environment_variable(var_name: str) -> Optional[str]:
    return os.environ.get(var_name)

def validate_list(input_list: List[Any]) -> bool:
    return isinstance(input_list, list) and all(isinstance(item, (int, str, float, bool)) for item in input_list)

def validate_dict(input_dict: Dict[str, Any]) -> bool:
    return isinstance(input_dict, dict) and all(isinstance(key, str) for key in input_dict.keys())