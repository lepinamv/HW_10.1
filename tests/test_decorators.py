import pytest

from src.decorators import log


# Проверка корректности успешного выполнения функции и записи в файл
def test_log_file(tmp_path):
    log_file = tmp_path / "test.log"

    @log(filename=str(log_file))
    def my_function(x, y):
        return x + y

    assert my_function(1, 2) == 3
    assert "my_function ok" in open(str(log_file)).read()


# Проверка корректности успешного выполнения функции и вывода в консоль
def test_log_console(capsys):
    @log(filename=None)
    def my_function_new(x, y):
        return x + y

    my_function_new(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function_new ok\n"


# Проверка возникновения ошибки при выполнении функции и записи в файл
def test_log_file_error(tmp_path):
    log_file = tmp_path / "test.log"

    @log(filename=str(log_file))
    def my_function(x, y):
        return x + y

    with pytest.raises(TypeError):
        my_function(1, "2")
    with open(str(log_file), "r") as f:
        content = f.read()
    assert "my_function error: TypeError" in content
    assert "Inputs: (1, '2'), {}" in content


# Проверка возникновения ошибки при выполнении функции и вывода в консоль
def test_log_console_error(capsys):
    @log(filename=None)
    def my_function(x, y):
        return x + y

    with pytest.raises(TypeError):
        my_function(1, "3")
    captured = capsys.readouterr()
    assert captured.out == "my_function error: TypeError. Inputs: (1, '3'), {}\n"
