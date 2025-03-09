import json
from pathlib import Path

from src.utils import read_json_file


def test_read_json_file() -> None:
    """Тест конвертации файла json или его отсутствия"""
    file_path = str(Path(__file__).parent.parent / "data/operations.json")
    test_no_file = read_json_file()
    test_file = read_json_file(file_path)
    assert test_no_file == []
    with open(file_path, "r", encoding="utf-8") as file:
        expected_data = json.load(file)
    assert test_file == expected_data
