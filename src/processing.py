def filter_by_state(sorting_list: list, key='EXECUTED') -> list:
    """Сортировка списка словарей по ключу state"""
    sorted_list = []
    for s in sorting_list:
        if s['state'] == key:
            sorted_list.append(s)
    return sorted_list

def sort_by_date(sorting_list: list, route=True) -> list:
    """Сортировка списка словарей по дате"""
    sorted_list = sorted(sorting_list, key=lambda s: s['date'], reverse=route)
    return sorted_list

#Проверка
#[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
