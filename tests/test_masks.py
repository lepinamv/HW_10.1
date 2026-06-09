import pytest

from src.masks import get_mask_account, get_mask_card_number


# ТЕСТИРОВАНИЕ get_mask_card_number
# Тестирование правильности маскирования номера карты
def test_get_mask_card_number(number: int) -> None:
    assert get_mask_card_number(number) == "7000 79** **** 6361"


# Проверка работы функции на различных входных форматах номеров карт, в т.ч., когда номер карты отсутствует.
@pytest.mark.parametrize("test_card_number", ["5105 1051 0510 5100", "abcdefghijklmnop", 378282246310005, ""])
def test_get_mask_card_number_error(test_card_number: int) -> None:
    with pytest.raises(ValueError, match="Номер должен состоять из 16 цифр"):
        get_mask_card_number(test_card_number)


# ТЕСТИРОВАНИЕ get_mask_account
# Тестирование правильности маскирования номера счета
def test_get_mask_account(account: int) -> None:
    assert get_mask_account(account) == "**4305"


# Проверка работы функции с различными форматами и длинами номеров счетов, в т.ч., когда номер счета отсутствует.
@pytest.mark.parametrize(
    "test_account_number", ["73654 10843 01358 74305", "abcde fghij klmno pqrst", 736541084301358743, ""]
)
def test_get_mask_account_error(test_account_number: int) -> None:
    with pytest.raises(ValueError, match="Номер должен состоять из 20 цифр"):
        get_mask_account(test_account_number)
