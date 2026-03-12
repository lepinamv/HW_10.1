def filter_by_state(sorting_list: list, key: str = "EXECUTED") -> list:
    """Сортировка списка словарей по ключу state"""
    sorted_list = []
    for dictionary in sorting_list:
        if dictionary["state"] == key:
            sorted_list.append(dictionary)
            if "state" not in dictionary:
                raise KeyError("Ключ state отсутствует")
    return sorted_list


def sort_by_date(sorting_list: list, route: bool = True) -> list:
    """Сортировка списка словарей по дате"""
    for dictionary in sorting_list:
        if "date" not in dictionary:
            raise KeyError("Ключ date отсутствует")
        elif "-" not in dictionary["date"] and len(dictionary["date"]) != 10:
            raise KeyError("Неверный формат даты")
    sorted_list = sorted(sorting_list, key=lambda dictionary: dictionary["date"], reverse=route)
    return sorted_list
