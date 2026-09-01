from pathlib import Path

import pandas as pd


def get_transactions_from_csv(file_path: str, delimiter: str = ";") -> list:
    """Получение списка транзакций из csv файла"""
    if not Path(file_path).suffix.lower() == ".csv":
        print("Файл не является CSV")
        return []
    try:
        transactions_from_csv = pd.read_csv(file_path, delimiter=delimiter)
    except (FileNotFoundError, pd.errors.EmptyDataError, ValueError) as e:
        print(f"Ошибка {e}")
        result = []
    except Exception as e:
        print(f"Неизвестная ошибка {e}")
        result = []
    else:
        result = transactions_from_csv.to_dict(orient="records")
    return result


# project_root = Path(__file__).parent.parent
# data_dir = project_root / "data"
# data_dir.mkdir(exist_ok=True)
# csv_file = data_dir / "transactions.csv"
#
# result = get_transactions_from_csv(csv_file)
# print(result[:5])


def get_transactions_from_excel(file_path: str) -> list:
    """Получение списка транзакций из excel файла"""
    if not Path(file_path).suffix.lower() in (".xlsx", ".xlsm", ".xlsb", ".xls"):
        print("Файл не является Excel")
        return []
    try:
        transactions_from_excel = pd.read_excel(file_path)
    except (FileNotFoundError, pd.errors.EmptyDataError, ValueError) as e:
        print(f"Ошибка {e}")
        result = []
    except Exception as e:
        print(f"Неизвестная ошибка {e}")
        result = []
    else:
        result = transactions_from_excel.to_dict(orient="records")
    return result


# project_root = Path(__file__).parent.parent
# data_dir = project_root / "data"
# data_dir.mkdir(exist_ok=True)
# xlsx_file = data_dir / "transactions_excel.xlsx"
#
# result = get_transactions_from_excel(xlsx_file)
# print(result[:5])
