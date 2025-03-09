import os.path

from src.external_api import convert_currency_for_rub
from src.utils import read_json_file

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    list_data = read_json_file(ROOT_DIR +"data/operations.json")
    for data in list_data:
        sum_currency = convert_currency_for_rub(data)
        print(sum_currency)
