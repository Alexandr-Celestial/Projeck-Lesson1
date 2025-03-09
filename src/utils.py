import json


def read_json_file(file_path: str = "") -> list:
    """Функция читает список словарей и данными о финансовых транзакциях"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data_json = json.load(f)
        return list(data_json)
    except FileNotFoundError:
        print(f"Error: File not found ad {file_path}")
        return []
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {file_path}")
        return []
    except Exception as e:
        print(f"Error: An unexpected error occurred {e}")
        return []
