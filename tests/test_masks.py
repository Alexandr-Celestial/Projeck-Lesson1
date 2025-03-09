import os

import pytest

from src.masks import get_mask_account, get_mask_card_number

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@pytest.mark.parametrize(
    "card_number, expected", [(1234567898123456, "1234 56** **** 3456"), (1111222233334444, "1111 22** **** 4444")]
)
def test_get_mask_card_number(card_number: int, expected: str) -> None:
    """Функция тестирует правильность маскировки номера карты"""
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("account_number, expected", [(1234567898, "**7898"), (9874563212, "**3212")])
def test_get_mask_account(account_number: int, expected: str) -> None:
    """Функция тестирует правильность маскировки номера счета"""
    assert get_mask_account(account_number) == expected


def test_get_mask_card_number_invalid_length() -> None:
    """Функция проверяет на вывод ValueError при указании неверной длины номера карты"""
    with pytest.raises(ValueError):
        get_mask_card_number(12345)
