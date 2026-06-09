import pytest

from src.processing import filter_by_state, sort_by_date


# ТЕСТИРОВАНИЕ filter_by_state
# Тестирование фильтрации списка словарей по заданному статусу state
@pytest.mark.parametrize(
    "key_test, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
    ],
)
def test_filter_by_state(test_sorting_list: list, key_test: str, expected: list) -> None:
    assert filter_by_state(test_sorting_list, key_test) == expected


# Тестирование ошибки
def test_filter_by_state_error() -> None:
    with pytest.raises(KeyError):
        filter_by_state(
            [
                {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "date": "2018-06-30T02:08:58.425572"},
            ]
        )


# Тестирование отличных списков: отсутствие в словарях ключа со статусом EXECUTED и CANCELED, пустой список
def test_filter_by_state_list_other_state(test_sorting_list_other_state: list) -> None:
    assert filter_by_state(test_sorting_list_other_state) == []


def test_filter_by_state_list_empty() -> None:
    assert filter_by_state([]) == []


# ТЕСТИРОВАНИЕ sort_by_date
# Тестирование сортировки списка словарей по датам в порядке убывания и возрастания
@pytest.mark.parametrize(
    "route, expected",
    [
        (
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date(test_sorting_list: list, route: bool, expected: list) -> None:
    assert sort_by_date(test_sorting_list, route) == expected


# Проверка корректности сортировки при одинаковых датах
def test_sort_by_date_list_one_date(test_list_one_date: list) -> None:
    assert sort_by_date(test_list_one_date) == test_list_one_date


# Тестирование ошибки
def test_sort_by_date_error() -> None:
    with pytest.raises(KeyError):
        sort_by_date(
            [
                {"id": 41428829, "dates": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "dates": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "dates": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "dates": "2018-10-14T08:21:33.419441"},
            ]
        )


# Тесты на работу функции с некорректными или нестандартными форматами дат
def test_sort_by_date_different_format() -> None:
    with pytest.raises(KeyError):
        sort_by_date(
            [
                {"id": 2, "date": "2018-06-30"},
                {"id": 3, "date": "12.09.2018"},
                {"id": 4, "date": "2019/01/15"},
                {"id": 5, "date": "03 Jul 2019"},
                {"id": 1, "date": "2019-07-03T18:35:29.512364"},
            ]
        )


def test_sort_by_date_list_empty() -> None:
    assert sort_by_date([]) == []
