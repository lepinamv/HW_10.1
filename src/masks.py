def get_mask_card_number(card_number: int) -> str:
    """Маскировка номера карты в формате XXXX XX** **** XXXX"""
    list_card_number = [int(digit) for digit in str(card_number)]
    mask_card_number = list_card_number[:4] + [" "] + list_card_number[4:6] + ["** **** "] + list_card_number[-4:]
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
    list_mask_account = [int(digit) for digit in str(account_number)]
    mask_account = ["**"] + list_mask_account[-4:]
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
