import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "info_number, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ],
)
def test_mask_account_card(info_number: str, expected: str):
    """Тестирование функции с различными типами карт и счетов"""
    assert mask_account_card(info_number) == expected


@pytest.mark.parametrize(
    "str_date, expected", [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2023-12-25T10:00:00.000000", "25.12.2023")]
)
def test_get_date(str_date, expected):
    """Тестирование функции с различными типами данных"""
    assert get_date(str_date) == expected
