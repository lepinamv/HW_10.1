import pytest


# Фикстура для проверки номера карты
@pytest.fixture
def number() -> int:
    return 7000792289606361


# Фикстура для проверки номера счета
@pytest.fixture
def account() -> int:
    return 73654108430135874305


# Фикстура для проверки корректности распознавания и применения нужного типа маскировки
@pytest.fixture
def card_number() -> str:
    return "Maestro 1596837868705199"


@pytest.fixture
def account_number() -> str:
    return "Счет 64686473678894779589"


# Тестируемый список словарей
@pytest.fixture
def test_sorting_list() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


# Список словарей, в которых state != EXECUTED or CANCELED
@pytest.fixture
def test_sorting_list_other_state() -> list:
    return [
        {"id": 41428829, "state": "Pending", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "Failed", "date": "2018-09-12T21:27:25.241689"},
    ]


# Список с одинаковыми датами
@pytest.fixture
def test_list_one_date() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
    ]


# Фикстура для использования разных форматов дат
@pytest.fixture
def test_dates() -> list:
    return [
        {"id": 1, "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "date": "2018-06-30"},
        {"id": 3, "date": "12.09.2018"},
        {"id": 4, "date": "2019/01/15"},
        {"id": 5, "date": "03 Jul 2019"},
    ]
