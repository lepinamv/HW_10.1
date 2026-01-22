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


def get_date(date: str) -> str:
    """Меняет формат даты на DD.MM.YYYY"""
    date_pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
    match = re.search(date_pattern, date)
    if match:
        formated_date = match.group('day') + "." + match.group('month') + "." + match.group('year')
    return formated_date


# Проверка:
print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Счет 35383033474447895560"))
print(mask_account_card("Visa Classic 6831982476737658"))
print(mask_account_card("Visa Platinum 8990922113665229"))
print(mask_account_card("Visa Gold 5999414228426353"))
print(mask_account_card("Счет 73654108430135874305"))

# print(mask_account_card("Счет 784304305"))

print(get_date("2024-03-11T02:26:18.671407"))
