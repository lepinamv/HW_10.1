from unittest.mock import patch

from src.external_api import currency_conversion


def test_currency_conversion_success():
    """Тестирование с использованием patch (имитация ответа от сервера)"""

    transactions = [
        {"operationAmount": {"amount": "1000.00", "currency": {"code": "RUB"}}},
        {"operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}},
        {"operationAmount": {"amount": "50.00", "currency": {"code": "EUR"}}},
    ]

    with patch("src.external_api.get_exchange_rate") as mock_rate:
        mock_rate.side_effect = [75.50, 89.50]
        result = currency_conversion(transactions)
        assert result == 13025.0


def test_currency_conversion_all_invalid():
    """Тестирование некорректных операций"""

    transactions = [
        {"operationAmount": {"amount": "invalid", "currency": {"code": "RUB"}}},
        {"operationAmount": {"amount": "100.00"}},  # Нет currency
        {"operationAmount": {"currency": {"code": "USD"}}},  # Нет amount
        {"description": "Просто описание"},
        {},
        None,
    ]

    result = currency_conversion(transactions, usd_rate=75.50, eur_rate=89.50)
    assert result == 0
