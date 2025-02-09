from src.widget import mask_account_card, get_date

if __name__ == "__main__":
    test_card_1 = mask_account_card("Maestro 1596837868705199")
    test_card_2 = mask_account_card("Счет 64686473678894779589")
    test_card_3 = mask_account_card("Visa Platinum 8990922113665229")
    print(test_card_1)
    print(test_card_2)
    print(test_card_3)
    test_date = get_date("2024-03-11T02:26:18.671407")
    print(test_date)
