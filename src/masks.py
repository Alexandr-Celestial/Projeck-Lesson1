def get_mask_card_number(card_number: int) -> str:
    """Принимает на вход номер карты и возвращает её маску"""
    card_str = str(card_number)
    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


def get_mask_account(account_number: int) -> str:
    """Принимает на вход номер счета и возвращает его маску"""
    account_number_str = str(account_number)
    return f"**{account_number_str[-4:]}"
