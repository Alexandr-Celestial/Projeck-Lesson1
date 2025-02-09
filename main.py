from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

test_data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
if __name__ == "__main__":
    test_maestro = mask_account_card("Maestro 1596837868705199")
    test_account = mask_account_card("Счет 64686473678894779589")
    test_visa_platinum = mask_account_card("Visa Platinum 8990922113665229")
    print(test_maestro)
    print(test_account)
    print(test_visa_platinum)
    test_date = get_date("2024-03-11T02:26:18.671407")
    print(test_date)
    test_filter = filter_by_state(test_data)
    print(test_filter)
    test_sort = sort_by_date(test_data, reverse=True)
    print(test_sort)
