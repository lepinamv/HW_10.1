from typing import Iterator


transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    """Функция возвращающая итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной"""
    #return (transaction for transaction in transactions
            #if transaction["operationAmount"]["currency"]["code"] == currency)
    for transaction in transactions:
        try:
            transaction_currency = transaction["operationAmount"]["currency"]["code"]
        except KeyError:
            raise KeyError(f"В транзакции {transaction.get('id', 'неизвестный ID')}  отсутствует поле валюты")
        if transaction_currency != currency:
            raise ValueError(f"Валюта транзакции {transaction_currency} не соответствует заданной {currency}")
        yield transaction

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """Генератор, который возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        if "description" not in transaction:
            raise KeyError(f"В транзакции {transaction.get('id', 'неизвестный ID')} отсутствует поле 'description'")
        yield transaction["description"]


descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))


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
        card_number = (card_number_str[0:4] + " " + card_number_str[4:8] + " " + card_number_str[8:12] + " " + card_number_str[12:16])
        yield card_number

for card_number in card_number_generator(1, 5):
    print(card_number)