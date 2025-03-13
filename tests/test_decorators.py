from typing import Any

import pytest

from src.decorators import log


def test_log_success(capsys: Any) -> None:
    """Тест успешного выполнения функции с логированием в консоль"""

    @log()
    def example_function() -> str:
        """Пример функции для логирования в консоль"""
        print("Hello, world")
        return "Success"

    result = example_function()
    captured = capsys.readouterr()
    assert result == "Success"
    assert "Начало выполнения функции example_function с аргументами: args=(), kwargs={}" in captured.out
    assert "Функция example_function завершилась успешно. Результат: Success" in captured.out


def test_log_exception(capsys: Any) -> None:
    """Тест обработки исключения с логированием в консоль"""

    @log()
    def example_function() -> None:
        """Пример функции для логирования в консоль"""
        raise ValueError("Test exception")

    with pytest.raises(ValueError):
        example_function()
    captured = capsys.readouterr()
    assert "Начало выполнения функции example_function" in captured.out


def test_log_in_file(tmp_path: Any) -> None:
    """Тест логирования в файл"""
    file_path = tmp_path / "log.txt"

    @log(filename=str(file_path))
    def example_function() -> str:
        """Пример функции для логирования в файл"""
        return "Success"

    example_function()
    with open(file_path, "r", encoding="utf-8") as f:
        log_content = f.read()
    assert "Начало выполнения функции example_function" in log_content
    assert "Функция example_function завершилась успешно. Результат: Success" in log_content


def test_log_exception_to_file(tmp_path: Any) -> None:
    """Тест логирования исключения в файл"""
    file_path = tmp_path / "log.txt"

    @log(filename=str(file_path))
    def example_function() -> None:
        """Пример функции для логирования исключения в файл"""
        raise ValueError("Test exception")

    with pytest.raises(ValueError):
        example_function()
    with open(file_path, "r", encoding="utf-8") as f:
        log_content = f.read()
    assert "Начало выполнения функции example_function" in log_content
    assert "Функция example_function завершилась с ошибкой: Test exception" in log_content
