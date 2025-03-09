import os
from unittest.mock import Mock, patch

import pytest

from src.external_api import convert_currency_for_rub, url


def test_convert_currency_for_rub_rub() -> None:
    """Тест для проверки конвертации транзакции в RUB"""
    transaction = {"operationAmount": {"amount": 100, "currency": {"code": "RUB"}}}
    result = convert_currency_for_rub(transaction)
    assert result == 100.0


@pytest.mark.parametrize("currency, expected_rate", [("USD", 75.0), ("EUR", 85.0)])
def test_convert_currency_for_rub_foreign(currency: str, expected_rate: float) -> None:
    """Тест для проверки конвертации транзакций в EUR и USD"""
    with patch("src.external_api.requests.get") as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": expected_rate * 100}
        mock_get.return_value = mock_response

        os.environ["API_KEY"] = "test_key"

        transaction = {"operationAmount": {"amount": 100, "currency": {"code": currency}}}
        result = convert_currency_for_rub(transaction)
        assert result == expected_rate * 100
        mock_get.assert_called_once_with(
            url, headers={"API_KEY": "test_key"}, params={"to": "RUB", "from": currency, "amount": 100.0}
        )


def test_convert_currency_for_rub_unsupported_currency() -> None:
    """Тест для проверки с неподдерживаемой валютой CNY"""
    transaction = {"operationAmount": {"amount": 100, "currency": {"code": "CNY"}}}
    with pytest.raises(ValueError, match="Unsupported currency: CNY"):
        convert_currency_for_rub(transaction)
