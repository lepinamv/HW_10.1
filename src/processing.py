def filter_by_state(sorting_list: list, key: str = 'EXECUTED') -> list:
    """Сортировка списка словарей по ключу state"""
    sorted_list = []
    for dictionary in sorting_list:
        if dictionary['state'] == key:
            sorted_list.append(dictionary)
    return sorted_list


def sort_by_date(sorting_list: list, route: bool = True) -> list:
    """Сортировка списка словарей по дате"""
    sorted_list = sorted(sorting_list, key=lambda dictionary: dictionary['date'], reverse=route)
    return sorted_list
