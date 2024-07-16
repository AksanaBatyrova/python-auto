"""Homework 20"""

# Покройте тестами програмы: "Библиотека" и "Банковский вклад" из домашней
# работы №11:

# Создайте отдельный модуль для тестов.
# Импортируйте функции из модуля.
# Напишите тесты на проверку работоспособности приложения.
# Тесты должны проверять как положительный результат, так и отрицательный.
# Тесты запускаются с помощью unittest

import unittest
from homework12.task1_library import Book, User


class TestLibrary(unittest.TestCase):
    """Class for testing Library task"""
    def setUp(self):
        self.allan_poe_raven = Book("The Raven", "Edgar Allan Poe", 6,
                                    9788506007914)
        self.johann_goethe_faust = Book("Faust, a Tragedy",
                                        "Johann Wolfgang von Goethe",
                                        165, 1503262146)
        self.user1 = User("John")
        self.user2 = User("Jane")

    def test_book_pages_amount(self):
        self.assertEqual(self.allan_poe_raven.get_pages(), 6)

    def test_book_isbn(self):
        self.assertEqual(self.johann_goethe_faust.get_isbn(), 1503262146)

    def test_reserve_book(self):
        self.assertEqual(
            self.user1.reserve_book(self.allan_poe_raven),
            "You've reserved 'The Raven' by Edgar Allan Poe")

    def test_is_book_reserved(self):
        self.user1.reserve_book(self.allan_poe_raven)
        self.assertTrue(self.allan_poe_raven.is_reserved)

    def test_reserved_book(self):
        self.user1.reserve_book(self.johann_goethe_faust)
        self.assertEqual(
            self.user2.reserve_book(self.johann_goethe_faust),
            "'Faust, a Tragedy' by Johann Wolfgang von Goethe is "
            "reserved by another user")

    def test_return_book(self):
        self.user1.reserve_book(self.allan_poe_raven)
        self.assertEqual(
            self.user2.return_book(self.allan_poe_raven),
            "You've returned 'The Raven' by Edgar Allan Poe")

    def test_returned_book(self):
        self.user2.reserve_book(self.johann_goethe_faust)
        self.user2.return_book(self.johann_goethe_faust)
        self.assertEqual(
            self.user2.return_book(self.johann_goethe_faust),
            "This book is free, nothing to return")


if __name__ == '__main__':
    unittest.main()
