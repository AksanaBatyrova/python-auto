"""Homework 12. Task 2 Bank deposit"""

# Банковский вклад
# Создайте класс вклад. Который содержит необходимые поля и методы, например
# сумма вклада и его срок. Пользователь делает вклад в размере N рублей сроком
# на R лет под 10% годовых (вклад с возможностью ежемесячной капитализации -
# это означает, что проценты прибавляются к сумме вклада ежемесячно). Написать
# класс Bank, метод deposit принимает аргументы N и R, и возвращает сумму,
# которая будет на счету пользователя.

# https://myfin.by/wiki/term/kapitalizaciya-procentov


class Bank:
    """This class describes bank and its services

    Arguments:
    amount: money deposited
    term: deposit term
    rate: interest rate (percent)

    Methods:
    deposit(): calculating how much bank client will receive when depositing at
    compound interest
    """

    def deposit(self, amount, term, rate):
        """This method is for calculating compound interest"""
        return round(amount * (1 + (rate/100) / 12) ** (12 * term), 2)

    def loan(self):
        """This method is used as workaround for Pylint
           R0903:too-few-public-methods"""


bank1 = Bank()

assert bank1.deposit(1000, 1, 10) == 1104.71
