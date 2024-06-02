"""This module is a homework 7 made by Aksana Batyrova"""

from typing import List

# Последовательность
# Дана последовательность целых чисел в виде массива. Определите, можно ли
# получить строго возрастающую последовательность, удалив из массива не более
# одного элемента.

# Примечание: последовательность a0, a1, ..., an считается строго возрастающей,
# если a0 < a1 < ... < an. Последовательность, содержащая только один элемент,
# также считается строго возрастающей.

# Примеры
# Для последовательности = [1, 3, 2, 1], вывод должен быть решение = False.

# В этом массиве нет ни одного элемента, который можно было бы удалить, чтобы
# получить строго возрастающую последовательность.

# Для последовательности = [1, 3, 2] вывод должен быть = True.

# Вы можете удалить 3 из массива, чтобы получить строго возрастающую
# последовательность [1, 2]. Альтернативно можно убрать 2, чтобы получить
# строго возрастающую последовательность [1, 3].

# solution([1, 2, 3])
# solution([1, 2, 1, 2])
# solution([1, 3, 2, 1])
# solution([1, 2, 3, 4, 5, 3, 5, 6])
# solution([40, 50, 60, 10, 20, 30])


def solution(sequence):
    """
    This function checks if possible to delete max 1 element from sequence
    to get strictly incremental sequence
    sequence: list of numbers

    return: True if possible to get strictly incremental sequence by deleting
    no or one element, False if not
    """
    if len(sequence) <= 3:
        return True
    x, y, *sequence = sequence
    difference = 0
    for z in sequence:
        if x < y < z:
            x, y = y, z
        else:
            difference += 1
        if difference > 1:
            return False
    return x < y


assert (solution([1, 3, 2])) is True
assert (solution([1, 2, 1, 2])) is False
assert (solution([1, 3, 2, 1])) is False
assert (solution([1, 2, 3, 4, 5, 3, 5, 6])) is False
assert (solution([40, 50, 60, 10, 20, 30])) is False

# Число на против
# Рассмотрим целые числа от 0 до n-1, записанные по окружности так, чтобы
# расстояние между любыми двумя соседними числами было одинаковым (обратите
# внимание, что 0 и n-1 тоже являются соседними).

# Учитывая n и first_number, найдите число, которое написано в радиально
# противоположной позиции от first_number.

# Примеры
# Для n = 10 и first_number = 2 вывод должен быть (n, first_number) = 7.


def opposite_number(n, first_number):
    """
    This function is counting the opposite number to first_number if they were
    written around a circle from 0 to n-1
    n: integer
    first_number: the number for which needs to find opposite

    return: number opposite to n
    """
    return int((n / 2 + first_number) % n)


print(opposite_number(10, 2))


# Validate
# Ваша задача написать программу, принимающее число - номер кредитной карты
# (число может быть четным или не четным). И проверяющей может ли такая карта
# существовать. Предусмотреть защиту от ввода букв, пустой строки и т.д.
# Примечания Алгоритм Луна

# Примеры
# validate(4561261212345464) #=> False
# validate(4561261212345467) #=> True

# Для проверки: https://www.paypalobjects.com/en_GB/vhelp/paypalmanager_help/
# credit_card_numbers.htm


def validate(card_number: int) -> bool:
    """
    This unction checks if credit card number exists
    card_number: 12-characters integer representing credit card number

    return: True if card exists, False if not
    """
    card_number_list = list(map(int, str(card_number)))
    each_second_elem: List[int] = []
    if len(card_number_list) % 2 == 0:
        a, b = 0, 1
    else:
        a, b = 1, 0
    for i in card_number_list[a::2]:
        if i*2 > 9:
            num = sum(map(int, str(i*2)))
            each_second_elem.append(num)
        else:
            each_second_elem.append(i*2)
    if (sum(each_second_elem) + sum(card_number_list[b::2])) % 10 == 0:
        return True
    return False


assert (validate(4561261212345464)) is False
assert (validate(4561261212345467)) is True
