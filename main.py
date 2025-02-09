from src.widget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date

if __name__ == "__main__":
    test_card_1 = mask_account_card("Maestro 1596837868705199")
    test_card_2 = mask_account_card("Счет 64686473678894779589")
    test_card_3 = mask_account_card("Visa Platinum 8990922113665229")
    print(test_card_1)
    print(test_card_2)
    print(test_card_3)
    test_date = get_date("2024-03-11T02:26:18.671407")
    print(test_date)
    test_data_1 = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    test_filter_by_state = filter_by_state(test_data_1, state='EXECUTED')
    print(test_data_1)
    test_data_2 = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    test_sort_by_date = sort_by_date(test_data_2, reverse=True)
    print(test_data_2)
