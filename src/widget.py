def mask_account_card(type_number: str) -> str:
    """Возвращает строку с замаскированным номером карты или счета"""
    list_numbers = re.findall(r'\d+', type_number)
    list_type = re.findall(r'\b[a-zA-Zа-яА-Я]+\b', type_number)
    number = int(list_numbers[0])
    if len(list_numbers[0]) == 16:
        result = list_type[0] + " " + masks.get_mask_card_number(number)
    elif len(list_numbers[0]) == 20:
        result = list_type[0] + " " + masks.get_mask_account(number)
    else:
        result = "Проверьте корректность входных данных"
    return result


