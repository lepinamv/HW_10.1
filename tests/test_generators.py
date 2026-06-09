import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_usd():
    transactions = [
        {"id": 1, "operationAmount": {"currency": {"code": "USD"}}, "description": "USD"},
        {"id": 2, "operationAmount": {"currency": {"code": "EUR"}}, "description": "EUR"},
    ]
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 1
    assert result[0]["id"] == 1


def test_empty_filter():
    result = list(filter_by_currency([], "USD"))
    assert result == []


def test_filter_missing_currency():
    transactions = [
        {"id": 1, "operationAmount": {"amount": "100"}},  # Нет currency
        {"id": 2, "operationAmount": {"currency": {"code": "USD"}}},
    ]

    with pytest.raises(KeyError, match="отсутствует поле валюты"):
        result = list(filter_by_currency(transactions, "USD"))


def test_descriptions():
    transactions = [{"description": "desc1"}, {"description": "desc2"}]
    result = list(transaction_descriptions(transactions))
    assert result == ["desc1", "desc2"]


def test_descriptions_empty():
    result = list(transaction_descriptions([]))
    assert result == []


def test_card_numbers():
    result = list(card_number_generator(1, 3))
    assert result == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003"
    ]


def test_card_number_format():
    result = list(card_number_generator(1234567890123456, 1234567890123456))
    assert result[0] == "1234 5678 9012 3456"
