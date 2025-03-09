import os

import requests
from dotenv import load_dotenv

load_dotenv(".env")
url = "https://api.apilayer.com/exchangerates_data/convert"


def convert_currency_for_rub(transaction: dict) -> float:
    """Функция для конвертации суммы транзакций в рубли"""
    currency = transaction["operationAmount"]["currency"]["code"]
    amount = float(transaction["operationAmount"]["amount"])

    if currency == "RUB":
        return amount
    elif currency in ["USD", "EUR"]:
        API_KEY = os.getenv("API_KEY")
        if not API_KEY:
            raise ValueError("API key not found environment variables")
        headers = {"API_KEY": API_KEY}
        parems = {"to": "RUB", "from": currency, "amount": amount}
        response = requests.get(url, headers=headers, params=parems)

        if response.status_code == 200:
            data = response.json()
            if "result" in data:
                return float(data["result"])
            else:
                raise ValueError("Result not found in response")
        else:
            raise ValueError(f"Failed to fetch exchange rates: {response.status_code}")
    else:
        raise ValueError(f"Unsupported currency: {currency}")
