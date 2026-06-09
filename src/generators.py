from typing import Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    """Функция возвращающая итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной"""
    for transaction in transactions:
        try:
            transaction_currency = transaction["operationAmount"]["currency"]["code"]
        except KeyError:
            raise KeyError(f"В транзакции {transaction.get('id', 'неизвестный ID')}  отсутствует поле валюты")
        if transaction_currency == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """Генератор, который возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        if "description" not in transaction:
            raise KeyError(f"В транзакции {transaction.get('id', 'неизвестный ID')} отсутствует поле 'description'")
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """Генератор номеров банковских карт в заданном диапазоне"""

    if start < 1:
        raise ValueError(f"Начальное значение не может быть меньше 1, получено {start}")
    if end > 9999999999999999:
        raise ValueError(f"Конечное значение не может быть больше 9999999999999999, получено {end}")
    if start > end:
        raise ValueError(f"Начальное значение ({start}) не может быть больше конечного ({end})")

    for number in range(start, end + 1):
        number_str = str(number)
        card_number_str = "0" * (16 - len(number_str)) + number_str
        card_number = (
                card_number_str[0:4] + " " + card_number_str[4:8] + " " + card_number_str[8:12] + " " +
                card_number_str[12:16]
        )
        yield card_number
