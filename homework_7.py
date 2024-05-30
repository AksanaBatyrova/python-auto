"""This module is a homework 7 made by Aksana Batyrova"""

import random

# Быки и коровы
# B классическом варианте игра рассчитана на двух игроков.
# Каждый из игроков задумывает и записывает тайное 4-значное число c
# неповторяющимися цифрами. Игрок, который начинает игру по жребию,
# делает первую попытку отгадать число.
# Попытка — это 4-значное число c неповторяющимися цифрами, сообщаемое
# противнику. Противник сообщает в ответ, сколько цифр угадано без
# совпадения c их позициями в тайном числе (то есть количество коров)
# и сколько угадано вплоть до позиции в тайном числе (то есть
# количество быков). При игре против компьютера игрок вводит
# комбинации одну за другой, пока не отгадает всю последовательность.
# Ваша задача реализовать программу, против которой можно сыграть
# в "Быки и коровы"


def generate_random_number():
    """function generating a number of 4 random unique digits"""
    number = []
    while len(number) < 4:
        digit = random.randint(0, 9)
        if digit not in number:
            number.append(digit)
    return number


def make_a_guess():
    """function asking user to enter their guess and checking it"""
    try:
        first_guess = int(input('Make a guess: '))
    except ValueError:
        print('Invalid input. Please enter only digits')
        result = make_a_guess()
    else:
        if len(list(map(int, str(first_guess)))) != 4:
            print('Invalid input. Please enter 4 unique digits')
            result = make_a_guess()
        if len(set(map(int, str(first_guess)))) != 4:
            print('Invalid input. Please enter 4 unique digits')
            result = make_a_guess()
        else:
            result = list(map(int, str(first_guess)))
    return result


def bulls_and_cows_game(answer, guess):
    """function describing 'cows and bulls' game"""
    cows = 0
    bulls = 0
    result = ''
    for i in range(4):
        if guess[i] == answer[i]:
            bulls += 1
        elif guess[i] in answer:
            cows += 1
    print(f'{cows} cows, {bulls} bulls')
    if bulls == 4:
        result = print('You win!')
    if bulls != 4:
        guess = make_a_guess()
        result = bulls_and_cows_game(answer, guess)
    return result


generated_answer = generate_random_number()
user_guess = make_a_guess()
bulls_and_cows_game(generated_answer, user_guess)


# Пирамида
# Мы можем визуализировать художественную пирамиду ASCII c N уровнями,
# напечатав N рядов звездочек, где верхний ряд имеет одну звездочку в
# центре, a каждый последующий ряд имеет две дополнительные звездочки
# c каждой стороны.

# Вот как это выглядит, когда N равно 3.

#   *
#  ***
# *****
# Вот как это выглядит, когда N равно 5.

#     *
#    ***
#   *****
#  *******
# *********
# Необходимо написать программу, которая генерирует такую пирамиду
# co значением N, равным 10


def pyramid(n):
    """print pyramid of * symbols"""
    for i in range(n):
        i = i * 2 - 1
        print(('*' * i).center(n * 2 - 1))


pyramid(10)


# Статуи
# Вы получили в подарок на день рождения статуи разных размеров,
# каждая статуя имеет неотрицательный целочисленный размер.
# Поскольку Вам нравится доводить вещи до совершенства, то
# необходимо расположить их от меньшего к большему, чтобы каждая
# статуя была больше предыдущей ровно на 1. Для этого Вам могут
# понадобиться дополнительные статуи. Определите количество
# отсутствующих статуй.

# Пример Для статуй = [6, 2, 3, 8] результат должен быть = 3.
# Иными словами, y Bac отсутствуют статуи размеров 4, 5 и 7.


statues_li = [6, 2, 3, 8]


def how_many_statues_needed(statues):
    """function checks how much statues needed to make whole line"""
    statues_ordered = sorted(statues)
    all_statues = list(range(statues_ordered[0], statues_ordered[-1]+1))
    return len(all_statues) - len(statues_ordered)


print(how_many_statues_needed(statues_li))
