from typing import Any, Dict, List


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Функция принимает список словарей и фильтрует по значению ключа 'state
    :param data:
    :param state:
    :return:
    """
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """
    Функция принимает список словарей и сортирует по дате(data)
    :param data:
    :param reverse:
    :return:
    """
    return sorted(data, key=lambda x: x["date"], reverse=reverse)
