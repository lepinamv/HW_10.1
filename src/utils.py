import json

import requests


def get_transaction_info(url):
    """Получение информации и сохранение списка транзакций"""
    transaction_info = []

    response = requests.get(url)
    status_code = response.status_code

    if status_code == 404:
        print("404 Файл не найден")

    elif status_code == 200:
        try:
            data = response.json()
            if not isinstance(data, list):
                print("Неверный формат данных")
            elif len(data) == 0:
                print("Отсутствует содержимое")
            else:
                transaction_info = data
        except json.JSONDecodeError:
            print("Недопустимые данные JSON")
    else:
        print(f"Запрос не был успешным. {status_code} - {response.reason}")
    with open("/Users/maria/my_project/new_project/data/operations.json", "w", encoding="utf-8") as f:
        json.dump(transaction_info, f, ensure_ascii=False, indent=2)
    return transaction_info


file_id = "1C0bUdTxUhck-7BoqXSR1wIEp33BH5YXy"
print(get_transaction_info(f"https://drive.google.com/uc?export=download&id={file_id}"))