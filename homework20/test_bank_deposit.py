"""Homework 20"""

# Покройте тестами програмы: "Библиотека" и "Банковский вклад" из домашней
# работы №11:

# Создайте отдельный модуль для тестов.
# Импортируйте функции из модуля.
# Напишите тесты на проверку работоспособности приложения.
# Тесты должны проверять как положительный результат, так и отрицательный.
# Тесты запускаются с помощью unittest


import unittest
from homework12.task2_bank_deposit import Bank


class TestDeposit(unittest.TestCase):
    """Class for testing Deposit method of the class Bank"""
    def setUp(self):
        self.bank = Bank()

    def test_valid_deposit(self):
        """test to check if output of a function is correct"""
        self.assertEqual(self.bank.deposit(1000, 1, 10), 1104.71)

    def test_invalid_amount(self):
        """test to check if function returns error if amount is below 0"""
        with self.assertRaises(ValueError) as context:
            self.bank.deposit(-1000, 1, 10)
        self.assertEqual(str(context.exception), 'Values should be positive')

    def test_invalid_term(self):
        """test to check if function returns error if term is below 0"""
        with self.assertRaises(ValueError) as context:
            self.bank.deposit(1000, -1, 10)
        self.assertEqual(str(context.exception), 'Values should be positive')

    def test_invalid_rate(self):
        """test to check if function returns error if rate is below 0"""
        with self.assertRaises(ValueError) as context:
            self.bank.deposit(1000, 1, -10)
        self.assertEqual(str(context.exception), 'Values should be positive')

    def test_invalid_type_amount(self):
        """test to check if function returns error if amount is not a number"""
        with self.assertRaises(ValueError) as context:
            self.bank.deposit('1000', 1, 10)
        self.assertEqual(str(context.exception), 'Values should be numbers')

    def test_invalid_type_term(self):
        """test to check if function returns error if term is not a number"""
        with self.assertRaises(ValueError) as context:
            self.bank.deposit(1000, '1', 10)
        self.assertEqual(str(context.exception), 'Values should be numbers')

    def test_invalid_type_rate(self):
        """test to check if function returns error if rate is not a number"""
        with self.assertRaises(ValueError) as context:
            self.bank.deposit(1000, 1, '10')
        self.assertEqual(str(context.exception), 'Values should be numbers')


if __name__ == '__main__':
    unittest.main()
