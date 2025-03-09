import logging, os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

masks_logger = logging.getLogger(__name__)
masks_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(os.path.join(ROOT_DIR, "logs/masks.log"), encoding="utf-8", mode="w")
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
masks_logger.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    """Принимает на вход номер карты и возвращает её маску"""
    card_str = str(card_number)
    try:
        if len(card_str) != 16:
            masks_logger.error(f"invalid card number length: {len(card_str)}")
            raise ValueError("Номер карты должен содержать 16 цифр")
        masked_card = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
        masks_logger.debug(f"Card number masked successfully")
        return masked_card
    except ValueError as e:
        masks_logger.exception(f"Error masking card number: {e}")
        raise


def get_mask_account(account_number: int) -> str:
    """Функция принимает на вход номер счета и возвращает маску"""
    account_number_str = str(account_number)
    masked_account = f"**{account_number_str[-4:]}"
    masks_logger.debug(f"Account number masked successfully")
    return masked_account
