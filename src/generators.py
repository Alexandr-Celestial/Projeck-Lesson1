from typing import Generator


def filter_by_currency(transactions: list[dict], currency_code: str) -> Generator:
    """Принимает список словарей с транзакциями и возвращает генератор для фильтрации транзакций по валюте"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Generator:
    """принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Generator:
    for number in range(start, stop + 1):
        card_number = f"{number:016d}"
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
