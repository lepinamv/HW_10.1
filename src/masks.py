import logging
from pathlib import Path

project_root = Path(__file__).parent.parent
logs_dir = project_root / "logs"
logs_dir.mkdir(exist_ok=True)
log_file = logs_dir / "masks.log"


logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(log_file, mode="w")
file_formatter = logging.Formatter("%(asctime)s: utils.py: %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: int) -> str:
    """Маскировка номера карты в формате XXXX XX** **** XXXX"""
    logger.info("Начало работы программы Маскировка номера карты")
    if not str(card_number).isdigit() == True:
        logger.error("Номер должен состоять из цифр")
        raise ValueError("Номер должен состоять из 16 цифр")
    list_card_number = [int(digit) for digit in str(card_number)]
    if len(list_card_number) != 16:
        logger.error("Длина номера карты не равна 16")
        raise ValueError("Номер должен состоять из 16 цифр")
    mask_card_number = list_card_number[:4] + [" "] + list_card_number[4:6] + ["** **** "] + list_card_number[-4:]
    logger.info("Маскировка номера карты выполнена")
    return "".join(map(str, mask_card_number))

    # Первоначальное решение
    # list_card_number = []
    # str_card_number = str(card_number)
    # str_mask_card_number = ""
    # for i in str_card_number:
    #     list_card_number.append(i)
    # mask_card_number = list_card_number[:4] + [" "] + list_card_number[4:6] + ["** **** "] + list_card_number[-4:]
    # for el in mask_card_number:
    #     str_mask_card_number += str(el)
    # return str_mask_card_number


# Проверка
# print(get_mask_card_number(7000792289606361))


def get_mask_account(account_number: int) -> str:
    """Маскировка номера счета в формате **XXXX"""
    logger.info("Начало работы программы Маскировка номера счета")
    if not str(account_number).isdigit() == True:
        logger.error("Номер должен состоять из цифр")
        raise ValueError("Номер должен состоять из 20 цифр")
    list_mask_account = [int(digit) for digit in str(account_number)]
    if len(list_mask_account) != 20:
        logger.error("Длина номера счета не равна 20")
        raise ValueError("Номер должен состоять из 20 цифр")
    mask_account = ["**"] + list_mask_account[-4:]
    logger.info("Маскировка номера счета выполнена успешно")
    return "".join(map(str, mask_account))

    # Первоначальное решение
    # list_mask_account = []
    # str_mask_account = ""
    # str_account_number = str(account_number)
    # for i in str_account_number:
    #     list_mask_account.append(i)
    # mask_account = ["**"] + list_mask_account[-4:]
    # for el in mask_account:
    #     str_mask_account += str(el)
    # return str_mask_account


# Проверка:
# print(get_mask_account(73654108430135874305))
