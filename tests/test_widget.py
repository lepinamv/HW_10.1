import pytest

from src.widget import get_date, mask_account_card


# ТЕСТИРОВАНИЕ mask_account_card
# Тесты для проверки корректноcти распознавания и применения нужного типа маскировки
def test_mask_card_correct(card_number: str) -> None:
    assert mask_account_card(card_number) == "Maestro 1596 83** **** 5199"


def test_mask_account_correct(account_number: str) -> None:
    assert mask_account_card(account_number) == "Счет **9589"


# Параметризованные тесты с разными типами карт и счетов для проверки универсальности функции.
@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(account_number: str, expected: str) -> None:
    assert mask_account_card(account_number) == expected


# Тестирование функции на обработку некорректных входных данных и проверка ее устойчивости к ошибкам.
@pytest.mark.parametrize(
    "invalid_data",
    [
        "MasterCard 73654 10843 01358 74305",
        "Счет abcdefghijklmnopqrst",
        "Visa 7365410843013587432",
        "",
        "7365410843013587432 Visa",
        "MasterCard 7365 1084 0135 7430",
    ],
)
def test_mask_account_card_error(invalid_data: str) -> None:
    with pytest.raises(ValueError, match="Проверьте корректность входных данных"):
        mask_account_card(invalid_data)


# ТЕСТИРОВАНИЕ get_date
# Тестирование правильности преобразования даты
@pytest.mark.parametrize(
    "date_yyyy_mm_dd, expected",
    [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2026-02-18T21:27:18.671407", "18.02.2026")],
)
def test_get_date(date_yyyy_mm_dd: str, expected: str) -> None:
    assert get_date(date_yyyy_mm_dd) == expected


# Проверка работы функции на различных входных форматах даты, включая граничные случаи и нестандартные строки с датами.
@pytest.mark.parametrize("invalid_date", ["11.03.2024", "2019/01/15", "", "date"])
def test_get_date_error(invalid_date: str) -> None:
    with pytest.raises(ValueError, match="Проверьте корректность входных данных"):
        get_date(invalid_date)
