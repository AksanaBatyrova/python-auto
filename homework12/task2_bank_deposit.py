"""Homework 12. Task 2 Bank deposit"""

# Банковский вклад
# Создайте класс вклад. Который содержит необходимые поля и методы, например
# сумма вклада и его срок. Пользователь делает вклад в размере N рублей сроком
# на R лет под 10% годовых (вклад с возможностью ежемесячной капитализации -
# это означает, что проценты прибавляются к сумме вклада ежемесячно). Написать
# класс Bank, метод deposit принимает аргументы N и R, и возвращает сумму,
# которая будет на счету пользователя.

# https://myfin.by/wiki/term/kapitalizaciya-procentov


class Deposit:
    """This class describes bank deposit

    Arguments:
    amount: money deposited
    term: deposit term
    """
    def __init__(self, amount, term):
        self.amount = amount
        self.term = term

    def withdraw_deposit(self):
        """This method is used as workaround for Pylint
           R0903:too-few-public-methods"""

    def topup_deposit(self):
        """This method is used as workaround for Pylint
           R0903:too-few-public-methods"""


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

    def loan(self):
        """This method is used as workaround for Pylint
           R0903:too-few-public-methods"""


bank1 = Bank()
assert bank1.deposit(1000, 2) == 1210
assert bank1.deposit(2690, 9) == 6342
