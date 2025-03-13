import csv

import pandas as pd


def read_csv_file(file_path: str) -> list[dict] | None:
    """Функция для чтения csv файла"""
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print(f"Ошибка: Файл {file_path} не найден")
        return None
    except csv.Error as e:
        print(f"Ошибка csv: {e}")
        return None
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return None


def read_excel_file(file_path: str) -> list[dict] | None:
    """Функция для чтения excel файла"""
    try:
        excel_data = pd.read_excel(file_path)
        return excel_data.to_dict("records")
    except FileNotFoundError:
        print(f"Ошибка: файл {file_path} не найден")
        return None
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return None
