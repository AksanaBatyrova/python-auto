"""Homework 13. Task2 Currency converter"""

# Конвертер валют
# Расширьте функционал класса Bank из домашней работы #11. Добавьте новый
# класс Currency, который умеет конвертировать различные валюты(USD, EUR, ...)
# в заданную валюту.

# bank = Bank(..)

# vasya = Person('USD', 10)
# petya = Person('EUR', 5)


class Bank:
    """This class describes bank and its services
    Arguments:
    amount: money deposited
    term: deposit term
    Methods:
    deposit(): calculating how much bank client will receive when depositing at
    compound interest
    """

    def deposit(self, n, r):
        """This method is for calculating compound interest"""
        return int(n*(1+0.1)**r)


class Currency(Bank):
    """This class describes currencies available for trading"""
    exchange_rates = {
        'USD': 1,
        'EUR': 0.93,
        'BYN': 3.26,
        'GBP': 0.79,
        'CAD': 1.38
    }

    @classmethod
    def exchange_currency(cls, sell, amount, buy='BYN'):
        """This method is for converting currency"""
        amount = round((amount * cls.exchange_rates[buy] /
                        cls.exchange_rates[sell]), 2)
        return amount, buy


class Person():
    """This class describes a customer of an exchange office"""
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount


bank = Bank()

vasya = Person("USD", 10)
petya = Person('EUR', 5)

# Если валюта не задана, то конвертация происходит в BYN:
assert Currency.exchange_currency(vasya.currency, vasya.amount) == (
    32.6, 'BYN'), 'Something went wrong'
assert Currency.exchange_currency(petya.currency, petya.amount) == (
    17.53, "BYN"), 'Something went wrong'

# Конвертация в заданную валюту BYN:
assert Currency.exchange_currency(vasya.currency, vasya.amount, 'EUR') == (
    9.3, "EUR"), 'Something went wrong'
assert Currency.exchange_currency(petya.currency, petya.amount, 'USD') == (
    5.38, "USD"), 'Something went wrong'
