from datetime import datetime

from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(info_number: str) -> str:
    """
    Функция, которая маскирует номер карты или счета
    :param info_number:
    :return:
    """
    parts_of_info_number = info_number.split()
    account_type = " ".join(parts_of_info_number[:-1])
    number = parts_of_info_number[-1]
    if len(number) == 16:
        mask_result = get_mask_card_number(int(number))
    else:
        mask_result = get_mask_account(int(number))

    return f"{account_type} {mask_result}"


def get_date(str_date: str) -> str:
    """
    Функция принимает строку с датой и преобразует в формат ДД.ММ.ГГ
    :param str_date:
    :return:
    """
    str_datetime = datetime.strptime(str_date, "%Y-%m-%dT%H:%M:%S.%f")

    return str(str_datetime.strftime("%d.%m.%Y"))