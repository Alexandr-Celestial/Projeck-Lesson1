import json, os
import logging


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

utils_logger = logging.getLogger(__name__)
utils_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(os.path.join(ROOT_DIR, "logs/utils.log"), encoding="utf-8", mode="w")
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)

def read_json_file(file_path: str = "") -> list:
    """Функция читает список словарей и данными о финансовых транзакциях"""
    try:
        utils_logger.debug(f"Attempting to read JSON file from {file_path}")
        with open(file_path, "r", encoding="utf-8") as file:
            data_json = json.load(file)
        if isinstance(data_json, list):
            utils_logger.debug(f"Successfully read JSON data from {file_path}")
            return data_json
        else:
            utils_logger.error(f"JSON data in {file_path} is not a list")
            return []
    except FileNotFoundError:
        utils_logger.error(f"Error: File not found ad {file_path}")
        return []
    except json.JSONDecodeError:
        utils_logger.error(f"Error: Could not decode JSON from {file_path}")
        return []
    except Exception as e:
        utils_logger.exception(f"Error: An unexpected error occurred {e}")
        return []