"""Deposit keywords"""

from robot.api.deco import keyword
from homework12.task2_bank_deposit import Bank


@keyword
def deposit(amount, term, rate):
    """This method return amount of pages"""
    return Bank.deposit(Bank, float(amount), float(term), float(rate))


@keyword
def deposit_strings(amount, term, rate):
    """Deposit function"""
    return Bank.deposit(Bank, amount, term, rate)
