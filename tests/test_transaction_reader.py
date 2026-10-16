from unittest.mock import patch
from src.transaction_reader import get_transactions_from_csv, get_transactions_from_excel
import pandas as pd


@patch('pandas.read_csv')
def test_get_transactions_from_csv(mock_read_csv):
    """Тестирование получения данных из csv файла"""
    test_df = pd.DataFrame({
        'id': [1],
        'state': ['EXECUTED'],
        'date': ['2026-09-01'],
        'amount': [000],
        'currency_name': ['Ruble'],
        'currency_code': ['RUB'],
        'from': ['Счет 123'],
        'to': ['Счет 789'],
        'description': ['Перевод']
    })
    mock_read_csv.return_value = test_df
    assert get_transactions_from_csv('any_path.csv') == test_df.to_dict(orient='records')
    mock_read_csv.assert_called_once_with('any_path.csv', delimiter=';')


def test_get_transactions_not_from_csv():
    """Тестирование получения данных НЕ из csv файла"""
    result = get_transactions_from_csv('file.xlsx')
    assert result == []


@patch('pandas.read_csv')
def test_csv_file_not_found(mock_read_csv):
    """Тестирование ошибки FileNotFoundError"""
    mock_read_csv.side_effect = FileNotFoundError
    assert get_transactions_from_csv('missing.csv') == []


@patch('pandas.read_csv')
def test_csv_empty_file(mock_read_csv):
    """Тестирование ошибки EmptyDataError"""
    mock_read_csv.side_effect = pd.errors.EmptyDataError
    assert get_transactions_from_csv('empty.csv') == []


@patch('pandas.read_csv')
def test_csv_value_error(mock_read_csv):
    """Тестирование ошибки ValueError"""
    mock_read_csv.side_effect = ValueError
    assert get_transactions_from_csv('value_error.csv') == []


@patch('pandas.read_csv')
def test_csv_unexpected_error(mock_read_csv):
    """Тестирование ошибки PermissionError"""
    mock_read_csv.side_effect = PermissionError
    assert get_transactions_from_csv('file.csv') == []
# Данный тип ошибки возникнет, если к файлу нет доступа или он используется другим приложением


@patch('pandas.read_excel')
def test_get_transactions_from_excel(mock_read_excel):
    """Тестирование получения данных из excel файла"""
    test_df = pd.DataFrame({
        'id': [2],
        'state': ['EXECUTED'],
        'date': ['2026-09-01'],
        'amount': [111],
        'currency_name': ['Ruble'],
        'currency_code': ['RUB'],
        'from': ['Счет 123'],
        'to': ['Счет 789'],
        'description': ['Перевод']
    })
    mock_read_excel.return_value = test_df
    assert get_transactions_from_excel('any_path.xlsx') == test_df.to_dict(orient='records')
    mock_read_excel.assert_called_once_with('any_path.xlsx')


def test_get_transactions_not_from_xlsx():
    """Тестирование получения данных НЕ из excel файла"""
    result = get_transactions_from_excel('file.csv')
    assert result == []


@patch('pandas.read_excel')
def test_excel_file_not_found(mock_read_excel):
    """Тестирование ошибки FileNotFoundError"""
    mock_read_excel.side_effect = FileNotFoundError
    assert get_transactions_from_excel('missing.xlsx') == []


@patch('pandas.read_excel')
def test_excel_empty_file(mock_read_excel):
    """Тестирование ошибки EmptyDataError"""
    mock_read_excel.side_effect = pd.errors.EmptyDataError
    assert get_transactions_from_excel('empty.xlsx') == []


@patch('pandas.read_excel')
def test_excel_value_error(mock_read_excel):
    """Тестирование ошибки ValueError"""
    mock_read_excel.side_effect = ValueError
    assert get_transactions_from_excel('value_error.xlsx') == []


@patch('pandas.read_excel')
def test_excel_unexpected_error(mock_read_excel):
    """Тестирование ошибки PermissionError"""
    mock_read_excel.side_effect = PermissionError
    assert get_transactions_from_excel('file.xlsx') == []
# Данный тип ошибки возникнет, если к файлу нет доступа или он используется другим приложением
