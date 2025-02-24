import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize("currency_code, expected", [("USD", 2), ("RUB", 1), ("CHY", 0)])
def test_filter_by_currency(sample_transactions: list, currency_code: str, expected: int) -> None:
    """Тестирование функции filter_by_currency"""
    transactions = list(filter_by_currency(sample_transactions, currency_code))
    assert len(transactions) == expected


def test_transaction_descriptions(sample_transactions: list) -> None:
    """Тестирование функции transaction_descriptions"""
    descriptions = list(transaction_descriptions(sample_transactions))
    assert len(descriptions) == len(sample_transactions)
    assert descriptions[0] == "Перевод организации"
    assert descriptions[1] == "Перевод со счета на счет"


def test_transaction_descriptions_empty() -> None:
    """Тестирование функции transaction_descriptions ч пустым списком"""
    descriptions = list(transaction_descriptions([]))
    assert len(descriptions) == 0


def test_card_number_generator() -> None:
    """Тестирование генератора card_number_generator"""
    generated_numbers = list(card_number_generator(1, 5))

    expected_numbers = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]

    assert generated_numbers == expected_numbers


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 1, ["0000 0000 0000 0001"]),
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (5, 1, []),
    ],
)
def test_card_number_generator_edge_values(start: int, stop: int, expected: list) -> None:
    """Тестирование генератора card_number_generator с крайними значениями"""
    generated = list(card_number_generator(start, stop))
    assert generated == expected
