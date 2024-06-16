"""Homework 13. Task 1 Cards deck"""

import random

# Колода карт
# Напишите программу которая содержит список карт, умеет их перемешивать и
# позволяет пользователю достать карту из колоды по ее номеру. Всего в колоде
# 54 карты. Класс Card содержит спискок номеров карт и список мастей.


class Card:
    """This class describes the playing card"""
    number_list = ['Joker', 'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen',
                   'King']
    suit_list = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __str__(self):
        if self.suit not in range(0, 3) or self.number not in range(0, 13):
            return 'Wrong card number'
        return f'{self.suit_list[self.suit]} {self.number_list[self.number]}'


class CardsDeck:
    """This class define cards deck
    Arguments:

    Methods:
    create_deck, shuffle, get
    """
    new_deck: list[str] = []

    def create_deck(self, cls):
        """This method is used to create cards deck"""
        for s in cls.suit_list:
            for n in cls.number_list:
                self.new_deck.append(f'{s} {n}')
        return self.new_deck

    def shuffle(self):
        """This method is used to shuffle cards deck"""
        self.new_deck = self.create_deck(Card)
        random.shuffle(self.new_deck)
        return self.new_deck

    def get(self, number):
        """This method is used to get a card by number"""
        if number not in range(0, 53):
            return 'Invalid card number'
        return self.new_deck[number]


deck = CardsDeck()
deck.shuffle()
card_number = int(input('Выберите карту из колоды в 54 карты:'))
card = deck.get(card_number)
print(f'You card is: {card}')

card_number = int(input('Выберите карту из колоды в 54 карты:'))
card = deck.get(card_number)
print(f'You card is: {card}')
