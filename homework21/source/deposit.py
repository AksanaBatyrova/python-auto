"""Deposit"""


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
        if (not isinstance(amount, int) or
                not isinstance(term, int) or
                not isinstance(rate, int)):
            raise ValueError('Values should be numbers')
        if amount < 0 or term < 0 or rate < 0:
            raise ValueError('Values should be positive')

        return round(amount * (1 + (rate/100) / 12) ** (12 * term), 2)
