"""Homework 21"""
# Покройте тестами програмы: "Библиотека" и "Банковский вклад" из домашней
# работы №11:

# Создайте отдельный модуль для тестов.
# Импортируйте функции из модуля.
# Напишите тесты на проверку работоспособности приложения.
# Тесты должны проверять как положительный результат, так и отрицательный.
# Тесты используют библиотеку logging\loguru для логирования
# Добавьте простой отчет к вашим тестам используя библиотеку pytest-html
# https://pytest-html.readthedocs.io/en/latest/
# https://pytest-with-eric.com/plugins/pytest-html/
# Тесты запускаются с помощью pytest
# Добавьте в файл .gitignore все файлы и папки которые генерирует в процессе
# своей работы pytest и pytest-html, те в репозитории с кодом не должно быть
# лишних файлов
# Есть возможность запустить тесты с разным уровнем логгирования без изменения
# кода(те передача уровня логгирования во время запуска тестов)
# Примерная структура проекта:
# homework21/
# .github/
# - ...
# - tests/
# -- test_<bank-app>.py    <-- Файл с тестами для тестирования банка
# -- test_<library-app>.py <-- Файл с тестами для тестирования библиотеки
# - source/
# -- <library>.py          <-- Модуль реализуюший функционал библиотеки
# -- <bank>.py             <-- Модуль реализуюший функционал банка
# .gitignore
# requirements.txt
# ...

# Note: Помимо кода, пулл реквест должен содержать в себе файл-репорт
# (прикрепленный к пулл реквесту) который генерируется по результатам запуска
# тестов.

# Note2: Названия файлов примерное


import pytest
from logs.logger import setup_logger

from homework21.source.deposit import Bank

logger = setup_logger(__name__)


@pytest.fixture
def bank():
    """Initialization of Bank"""
    return Bank()


def test_valid(bank):
    """test to check if output of a function is correct"""
    logger.info('Test 1. Verify that program is working correctly '
                'with valid data')
    assert bank.deposit(1000, 1, 10) == 1104.71


def test_invalid_amount(bank):
    """test to check if function return error if amount is below 0"""
    logger.info('Test 2. Verify that program return error if amount is '
                'negative')
    with pytest.raises(ValueError) as execinfo:
        bank.deposit(-1000, 1, 10)
    assert 'Values should be positive' in str(execinfo.value)


def test_invalid_term(bank):
    """test to check if function return error if term is below 0"""
    logger.info('Test 3. Verify that program return error if term is '
                'negative')
    with pytest.raises(ValueError) as execinfo:
        bank.deposit(1000, -1, 10)
    assert 'Values should be positive' in str(execinfo.value)


def test_invalid_rate(bank):
    """test to check if function returns error if rate is below 0"""
    logger.info('Test 4. Verify that program return error if rate is '
                'negative')
    with pytest.raises(ValueError) as execinfo:
        bank.deposit(1000, 1, -10)
    assert 'Values should be positive' in str(execinfo.value)


def test_invalid_type_amount(bank):
    """test to check if function returns error if amount is not a number"""
    logger.info('Test 5. Verify that program return error if amount is not a '
                'number')
    with pytest.raises(ValueError) as execinfo:
        bank.deposit('1000', 1, 10)
    assert 'Values should be numbers' in str(execinfo.value)


def test_invalid_type_term(bank):
    """test to check if function returns error if term is not a number"""
    logger.info('Test 6. Verify that program return error if term is not a '
                'number')
    with pytest.raises(ValueError) as execinfo:
        bank.deposit(1000, '1', 10)
    assert 'Values should be numbers' in str(execinfo.value)


def test_invalid_type_rate(bank):
    """test to check if function returns error if rate is not a number"""
    logger.info('Test 7. Verify that program return error if rate is not a '
                'number')
    with pytest.raises(ValueError) as execinfo:
        bank.deposit(1000, 1, '10')
    assert 'Values should be numbers' in str(execinfo.value)
