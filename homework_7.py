"""
Быки и коровы
B классическом варианте игра рассчитана на двух игроков.
Каждый из игроков задумывает и записывает тайное 4-значное число c
неповторяющимися цифрами. Игрок, который начинает игру по жребию,
делает первую попытку отгадать число.
Попытка — это 4-значное число c неповторяющимися цифрами, сообщаемое
противнику. Противник сообщает в ответ, сколько цифр угадано без
совпадения c их позициями в тайном числе (то есть количество коров)
и сколько угадано вплоть до позиции в тайном числе (то есть
количество быков). При игре против компьютера игрок вводит
комбинации одну за другой, пока не отгадает всю последовательность.
Ваша задача реализовать программу, против которой можно сыграть
в "Быки и коровы"
"""

ANSWER = 2310
guess = input('Make a guess: ')


def bulls_and_cows_game(answer, guess):
    # function describing cows and bulls game
    cows = 0
    bulls = 0
    answer_li = list(str(answer))
    guess_li = list(guess)
    for i in range(4):
        if guess_li[i] == answer_li[i]:
            bulls += 1
        elif guess_li[i] in answer_li:
            cows += 1
    print(f'{cows} cows, {bulls} bulls')
    if bulls != 4:
        guess = input('Make another guess: ')
        bulls_and_cows_game(answer, guess)
    elif bulls == 4:
        return 'You win!'


bulls_and_cows_game(ANSWER, guess)

"""
Пирамида
Мы можем визуализировать художественную пирамиду ASCII c N уровнями,
напечатав N рядов звездочек, где верхний ряд имеет одну звездочку в
центре, a каждый последующий ряд имеет две дополнительные звездочки
c каждой стороны.

Вот как это выглядит, когда N равно 3.

  *
 ***
*****
Вот как это выглядит, когда N равно 5.

    *
   ***
  *****
 *******
*********
Необходимо написать программу, которая генерирует такую пирамиду
co значением N, равным 10
"""


def pyramid(n):
    # print pyramid of * sumbols
    for i in range(n):
        i = i * 2 - 1
        print(('*' * i).center(n * 2 - 1))


pyramid(10)

"""
Статуи
Вы получили в подарок на день рождения статуи разных размеров,
каждая статуя имеет неотрицательный целочисленный размер.
Поскольку Вам нравится доводить вещи до совершенства, то
необходимо расположить их от меньшего к большему, чтобы каждая
статуя была больше предыдущей ровно на 1. Для этого Вам могут
понадобиться дополнительные статуи. Определите количество
отсутствующих статуй.

Пример Для статуй = [6, 2, 3, 8] результат должен быть = 3.
Иными словами, y Bac отсутствуют статуи размеров 4, 5 и 7.
"""

statues = [6, 2, 3, 8]


def how_many_statues_needed(statues):
    # functions check how much statues needed to make whole line
    statues_ordered = sorted(statues)
    all_statues = list(range(statues_ordered[0], statues_ordered[-1]+1))
    print(all_statues)
    print(len(all_statues) - len(statues_ordered))


how_many_statues_needed(statues)
