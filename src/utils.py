import json
import logging
from pathlib import Path

import requests

from config import OPERATIONS_JSON

project_root = Path(__file__).parent.parent
logs_dir = project_root / "logs"
logs_dir.mkdir(exist_ok=True)
log_file = logs_dir / "utils.log"


logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(log_file, mode="w")
file_formatter = logging.Formatter("%(asctime)s: utils.py: %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_transaction_info(url):
    """Получение информации и сохранение списка транзакций"""
    transaction_info = []
    logger.info("Запрос информации")
    response = requests.get(url)
    status_code = response.status_code

    if status_code == 404:
        logger.error("404 Файл не найден")
        print("404 Файл не найден")

    elif status_code == 200:
        logger.info("Запрос выполнен успешно")
        try:
            data = response.json()
            if not isinstance(data, list):
                logger.error("Неверный формат данных")
                print("Неверный формат данных")
            elif len(data) == 0:
                logger.error("Отсутствует содержимое")
                print("Отсутствует содержимое")
            else:
                logger.info("Данные получены")
                transaction_info = data
        except json.JSONDecodeError:
            logger.error("Недопустимые данные JSON")
            print("Недопустимые данные JSON")
    else:
        logger.error("Запрос не был успешным")
        print(f"Запрос не был успешным. {status_code} - {response.reason}")
    with OPERATIONS_JSON.open("w", encoding="utf-8") as f:
        json.dump(transaction_info, f, ensure_ascii=False, indent=2)
    return transaction_info


file_id = "1C0bUdTxUhck-7BoqXSR1wIEp33BH5YXy"
print(get_transaction_info(f"https://drive.google.com/uc?export=download&id={file_id}"))
