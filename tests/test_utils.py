import json
from unittest.mock import Mock, patch

from src.utils import get_transaction_info


def test_get_transaction_info_success():
    """Тестирование успешного выполнения запроса при помощи Mock"""

    expected = [{"operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}}}]

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = expected

    with patch("src.utils.requests.get", return_value=mock_response) as mock_get:
        test_url = "https://drive.google.com/uc?export=download&id=test_id"
        result = get_transaction_info(test_url)

        assert result == expected
        mock_get.assert_called_once_with(test_url)


@patch("src.utils.requests.get")
def test_get_transaction_info_success_patch(mock_get):
    """Тестирование успешного выполнения запроса при помощи patch"""

    test_data = [{"operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}}}]

    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = test_data
    test_url = "https://drive.google.com/uc?export=download&id=test_id"
    result = get_transaction_info(test_url)
    assert result == test_data
    mock_get.assert_called_once_with(test_url)


@patch("src.utils.requests.get")
def test_get_transaction_info_invalid(mock_get):
    """Тестирование при ошибке 404"""

    mock_response = mock_get.return_value
    mock_response.status_code = 404
    test_url = "https://drive.google.com/uc?export=download&id=test_id"
    result = get_transaction_info(test_url)
    assert result == []
    mock_get.assert_called_once_with(test_url)


@patch("src.utils.requests.get")
def test_get_transaction_info_not_list(mock_get):
    """Тестирование при ошибке Неверный формат данных"""

    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {"message": "Неверный формат данных"}

    test_url = "https://drive.google.com/uc?export=download&id=test_id"
    result = get_transaction_info(test_url)
    assert result == []
    mock_get.assert_called_once_with(test_url)


@patch("src.utils.requests.get")
def test_get_transaction_info_empty_list(mock_get):
    """Тестирование при ошибке Отсутствует содержимое"""

    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = []

    test_url = "https://drive.google.com/uc?export=download&id=test_id"
    result = get_transaction_info(test_url)
    assert result == []
    mock_get.assert_called_once_with(test_url)


@patch("src.utils.requests.get")
def test_get_transaction_info_invalid_json(mock_get):
    """Тестирование при ошибке Недопустимые данные JSON"""

    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.side_effect = json.JSONDecodeError("Invalid JSON", "", 0)

    test_url = "https://drive.google.com/uc?export=download&id=test_id"
    result = get_transaction_info(test_url)
    assert result == []
    mock_get.assert_called_once_with(test_url)
