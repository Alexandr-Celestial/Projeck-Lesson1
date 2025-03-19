import pytest

from src.search import count_categories, search_by_description


def test_search_by_description() -> None:
    """Тестирование функции search_by_description с поиском по строке"""
    transactions = [
        {"description": "Оплата в магазине"},
        {"description": "Оплата ЖКХ"},
        {"description": "Перевод на карту"},
    ]
    search_string = "магазин"
    expected_result: list[dict] = [{"description": "Оплата в магазине"}]
    assert search_by_description(transactions, search_string) == expected_result


def test_search_by_description_case_insensitive() -> None:
    """Тестирование функции search_by_description с регистрозависимым поиском"""
    transactions = [
        {"description": "Оплата в Магазине"},
        {"description": "Оплата ЖКХ"},
        {"description": "Перевод на карту"},
    ]
    search_string = "магазин"
    expected_result: list[dict] = [{"description": "Оплата в Магазине"}]
    assert search_by_description(transactions, search_string) == expected_result


def test_search_by_description_no_match() -> None:
    """Тестирование функции search_by_description рпи отсутствии совпадений"""
    transactions = [
        {"description": "Оплата в магазине"},
        {"description": "Оплата ЖКХ"},
        {"description": "Перевод на карту"},
    ]
    search_string = "холодильник"
    expected_result: list[dict] = []
    assert search_by_description(transactions, search_string) == expected_result


def test_count_categories() -> None:
    """Тестирование функции count_categories со счетом категорий"""
    transactions: list[dict] = [
        {"description": "Оплата в магазине"},
        {"description": "Оплата ЖКХ"},
        {"description": "Оплата в магазине"},
        {"description": "Перевод на карту"},
    ]
    assert count_categories(transactions) == {}


def test_count_categories_empty() -> None:
    """Тестирование функции count_categories с пустым списком транзакций"""
    transactions: list[dict] = []
    expected_result: dict[str, int] = {}
    assert count_categories(transactions) == expected_result


def test_count_categories_no_description() -> None:
    """Тестирование count_categories без описаний в транзакциях"""
    transactions: list[dict] = [{"id": 1}, {"id": 2}, {"id": 3}]
    expected_result: dict[str, int] = {}
    assert count_categories(transactions) == expected_result


@pytest.mark.parametrize(
    ("list_of_categories", "expected_result"),
    [
        (["Перевод организации"], {"Перевод организации": 1}),
        (
            ["Перевод организации", "Перевод со счета на счет"],
            {"Перевод организации": 1, "Перевод со счета на счет": 2},
        ),
    ],
)
def test_counter_categories(sample_transactions: list[dict], list_of_categories: list, expected_result: dict) -> None:
    """Тест функции"""
    assert count_categories(sample_transactions, list_of_categories) == expected_result
