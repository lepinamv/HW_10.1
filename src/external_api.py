import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

payload = {}
headers = {"apikey": API_KEY}


def get_exchange_rate(currency: str) -> float:
    """Получает курс валюты к рублю"""
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount=1"
    response = requests.get(url, headers=headers, data=payload)
    if response.status_code != 200:
        raise ValueError(f"Невозможно получить данные для {currency}")
    result = response.json()
    return result["info"]["rate"]


def currency_conversion(transactions: list, usd_rate: float = None, eur_rate: float = None) -> float:
    """Конвертирует транзакции в рубли"""
    amount = []

    if usd_rate is None:
        usd_rate = get_exchange_rate("USD")
        print(f"ставка usd_rate {usd_rate}")
    if eur_rate is None:
        eur_rate = get_exchange_rate("EUR")
        print(f"ставка eur_rate {eur_rate}")

    for transaction in transactions:
        try:
            currency = transaction["operationAmount"]["currency"]["code"]
            print(currency)
            amount_float = float(transaction["operationAmount"]["amount"])
            print(amount_float)
        except (KeyError, ValueError, TypeError):
            continue

        if currency == "RUB":
            amount.append(amount_float)
        elif currency == "USD":
            conv_usd_amount = amount_float * usd_rate
            amount.append(conv_usd_amount)
        elif currency == "EUR":
            conv_eur_amount = amount_float * eur_rate
            amount.append(conv_eur_amount)

    return sum(amount)


with open("/Users/maria/my_project/new_project/data/operations.json") as f:
    t = json.load(f)
result = currency_conversion(t)
print(f"Общая сумма платежей {result} руб.")
