import time
from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = "mylog.txt") -> Callable:
    """Декоратор автоматически логирует начало и конец выполнения функции, результаты или возникшие ошибки"""

    def wrapper(func: Callable) -> Callable:
        """Внутренняя функция-декоратор."""

        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            """Внутренняя функция-обертка с логированием."""
            time_start = time.time()
            try:
                result = func(*args, **kwargs)
                time_end = time.time()
                time_for_work = time_end - time_start
                if filename is not None:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as e:
                error_text = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if filename is not None:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(error_text + "\n")
                else:
                    print(error_text)
                raise

        return inner

    return wrapper
