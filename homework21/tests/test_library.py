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

from homework21.source.library import User, Book

logger = setup_logger(__name__)


@pytest.fixture
def create_user_1():
    """Fixture to create user Jane"""
    return User("Jane")


@pytest.fixture
def create_user_2():
    """Fixture to create user John"""
    return User('John')


@pytest.fixture
def create_book_1():
    """Fixture to create a book The Raven by Edgar Allan Poe"""
    return Book("The Raven", "Edgar Allan Poe", 6, 9788506007914)


@pytest.fixture
def create_book_2():
    """Fixture to create a book Faust, a Tragedy by Johann Wolfgang
       von Goethe"""
    return Book("Faust, a Tragedy", "Johann Wolfgang von Goethe",
                165, 1503262146)


def test_book_pages_amount(create_book_1):
    """test to check the work of 'get_pages' function"""
    logger.info('Test 1. Verify work of "get_pages" function')
    assert create_book_1.get_pages() == 6


def test_book_isbn(create_book_2):
    """test to check the work of 'get_isbn' function"""
    logger.info('Test 2. Verify work of "get_isbn" function')
    assert create_book_2.get_isbn() == 1503262146


def test_reserve_book(create_user_1, create_book_1):
    """test to check the work of 'reserve_book' function"""
    logger.info('Test 3. Verify return after book reservation')
    assert create_user_1.reserve_book(create_book_1) == (
        "You've reserved 'The Raven' by Edgar Allan Poe")


def test_is_book_reserved(create_user_1, create_book_1):
    """test to check the work of 'reserve_book' function"""
    logger.info('Test 4. Verify that book is reserved')
    create_user_1.reserve_book(create_book_1)
    assert create_book_1.is_reserved is True


def test_reserved_book(create_user_1, create_user_2, create_book_2):
    """test to check the work of 'reserve_book' function"""
    logger.info('Test 5. Verify return of the "reserve_book" if book is '
                'already reserved by another user')
    create_user_1.reserve_book(create_book_2)
    assert create_user_2.reserve_book(create_book_2) == (
        "'Faust, a Tragedy' by Johann Wolfgang von Goethe is "
        "reserved by another user")


def test_return_book(create_user_1, create_user_2, create_book_1):
    """test to check the work of 'return_book' function"""
    logger.info('Test 6. Verify return of the "return_book" function')
    create_user_1.reserve_book(create_book_1)
    assert create_user_2.return_book(create_book_1) == (
        "You've returned 'The Raven' by Edgar Allan Poe")


def test_returned_book(create_user_2, create_book_2):
    """test to check the work of 'return_book' function"""
    logger.info('Test 7. Verify return of the "return_book" if book has '
                'been already returned')
    create_user_2.reserve_book(create_book_2)
    create_user_2.return_book(create_book_2)
    assert create_user_2.return_book(create_book_2) == (
        "This book is free, nothing to return")
