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


def count_categories(transactions: list[dict]) -> dict:
    """Функция для подсчёта банковских операций по определённой категории"""
    categories_count: Counter[str] = Counter()
    for transaction in transactions:
        if "description" in transaction:
            description = transaction["description"]
            categories_count[description] += 1
    return dict(categories_count)
