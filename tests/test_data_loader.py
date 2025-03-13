from collections.abc import Callable
from unittest.mock import mock_open, patch

import pandas as pd

from src.data_loader import read_csv_file, read_excel_file


@patch("src.data_loader.open", new_callable=mock_open, read_data="")
def test_read_csv_file_success(mock_open: Callable) -> None:
    """Тест успешного чтения CSV файла."""
    result = read_csv_file("fake_path.csv")
    assert result == []


@patch("src.data_loader.open", side_effect=FileNotFoundError)
def test_read_csv_file_not_found(mock_open: Callable) -> None:
    """Тест обработки FileNotFoundError при чтении CSV."""
    result = read_csv_file("fake_path.csv")
    assert result is None


@patch("src.data_loader.open", new_callable=mock_open, read_data="")
def test_read_csv_file_empty(mock_open: Callable) -> None:
    """Тест чтения пустого CSV файла."""
    result = read_csv_file("fake_path.csv")
    assert result == []


@patch("pandas.read_excel")
def test_read_excel_file_success(mock_read_excel: pd.DataFrame) -> None:
    """Тест успешного чтения Excel файла."""
    mock_read_excel.return_value = pd.DataFrame([{"col1": "val1", "col2": "val2"}])
    result = read_excel_file("fake_path.xlsx")
    assert result == [{"col1": "val1", "col2": "val2"}]


@patch("pandas.read_excel", side_effect=FileNotFoundError)
def test_read_excel_file_not_found(mock_read_excel: pd.DataFrame) -> None:
    """Тест обработки FileNotFoundError при чтении Excel."""
    result = read_excel_file("fake_path.xlsx")
    assert result is None


@patch("pandas.read_excel")
def test_read_excel_file_empty(mock_read_excel: pd.DataFrame) -> None:
    """Тест чтения пустого Excel файла."""
    mock_read_excel.return_value = pd.DataFrame()
    result = read_excel_file("fake_path.xlsx")
    assert result == []
