import re
from collections import Counter


def search_by_description(transactions: list[dict], search_string: str) -> list[dict]:
    """Функция для поиска списка словарей по заданной строке"""
    pattern = re.compile(search_string, re.I)
    result = []
    for transaction in transactions:
        if pattern.search(transaction.get("description", "")):
            result.append(transaction)
    return result


def count_categories(transactions: list[dict], list_of_categories: list = []) -> dict:
    """Функция для подсчёта банковских операций по определённой категории"""
    transaction_categories = [
        transaction["description"]
        for transaction in transactions
        if "description" in transaction and transaction["description"] in list_of_categories
    ]
    return dict(Counter(transaction_categories))
