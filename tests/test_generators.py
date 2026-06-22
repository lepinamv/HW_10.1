import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_usd(transactions):
    result = filter_by_currency(transactions, "USD")
    result_list = list(result)  # список транзакций, отфильтрованных по usd
    # Проверяем количество отфильтрованных операций
    assert len(result_list) == 3
    # Проверяем, что все транзакции имеют валюту USD
    for transaction in result_list:
        assert transaction["operationAmount"]["currency"]["code"] == "USD"


@pytest.mark.parametrize(
    "currency, expected_ids",
    [
        ("USD", [939719570, 142264268, 895315941]),
        ("RUB", [873106923, 594226727]),
        ("EUR", []),
    ],
)
def test_filter_by_currency_parametrized(transactions, currency, expected_ids):
    result = filter_by_currency(transactions, currency)
    ids = [transaction["id"] for transaction in result]
    # Проверяем, что f-ия корректно фильтрует транзакции по заданной валюте и обрабатывает случаи,
    # когда транзакции в заданной валюте отсутствуют
    assert ids == expected_ids


def test_filter_by_currency_empty_list():
    result = list(filter_by_currency([], "USD"))
    # Проверяем, что f-ия корректно обрабатывает пустой список
    assert result == []


def test_filter_by_currency_missing_currency(transactions_missing_currency_and_description):
    # Проверяем, что f-ия корректно обрабатывает список, в котором отсутствует поле валюты
    with pytest.raises(KeyError, match="отсутствует поле валюты"):
        result = list(filter_by_currency(transactions_missing_currency_and_description, "USD"))


def test_transaction_descriptions(transactions, expected_descriptions):
    result = transaction_descriptions(transactions)
    list_result = list(result)  # список описаний каждой транзакции
    # Проверяем, используя фикстуру, что создается корректный список описаний каждой транзакции
    assert list_result == expected_descriptions


def test_transaction_descriptions_empty():
    result = list(transaction_descriptions([]))
    # Проверяем, что f-ия корректно обрабатывает пустой список
    assert result == []


def test_transaction_descriptions_missing_descriptions(transactions_missing_currency_and_description):
    # Проверяем, что f-ия корректно обрабатывает список, в котором отсутствует поле описание
    with pytest.raises(KeyError, match="отсутствует поле 'description'"):
        result = list(transaction_descriptions(transactions_missing_currency_and_description))


def test_card_number_generator(expected_card_number):
    # Проверяем, что генератор выдает правильные номера карт в заданном диапазоне
    generator = card_number_generator(1, 3)
    result = list(generator)
    assert len(result) == 3
    assert result == expected_card_number
    # Проверяем, что после завершения генератор выбрасывает StopIteration
    with pytest.raises(StopIteration):
        next(generator)
    # Проверяем корректность форматирования (через длину: 16 цифр + 3 пробела = 19 символов)
    for card in result:
        assert len(card) == 19


@pytest.mark.parametrize(
    "start, end",
    [
        (1, 1),  # Минимальное значение
        (9999999999999999, 9999999999999999),  # Максимальное значение
    ],
)
def test_card_number_boundary_values(start, end):
    # Проверяем граничные значения диапазона
    generator = card_number_generator(start, end)
    if start == end:
        result = list(generator)
        assert len(result) == 1
        if start == 1:
            assert result[0] == "0000 0000 0000 0001"
        elif start == 9999999999999999:
            assert result[0] == "9999 9999 9999 9999"
