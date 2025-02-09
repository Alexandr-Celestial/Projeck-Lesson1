def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция принимает список словарей и фильтрует по значению ключа 'state"""
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
    """Функция принимает список словарей и сортирует по дате(data)"""
    return sorted(data, key=lambda x: x["date"], reverse=reverse)
