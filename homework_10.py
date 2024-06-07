"""This module is a homework 7 made by Aksana Batyrova"""

from itertools import groupby

# Строки с заданным символом
# Напишите программу, которая бы работала следующим образом - находила символ
# "#" и если этот символ найден - удаляла предыдущий символ из строки. Ваша
# задача обработать строки с "#" символом.

# Примеры:

# "a#bc#d"        ==>  "bd"
# "abc#d##c"      ==>  "ac"
# "abc##d######"  ==>  ""
# "#######"       ==>  ""
# ""              ==>  ""


def strings_with_symbol(input_str):
    """This function call delete_elements function if there is no '#' elements
    in input string otherwise returns empty string

    input_str (str): input string

    return: calls delete_elements function if '#' is in input string,
            empty string instead
  """
    if "#" not in input_str:
        return ""
    str_list = list(input_str)
    if str_list[str_list.index("#")-1] != "#":
        str_list.remove(str_list[str_list.index("#")-1])
        str_list.remove("#")
        "".join(str_list)
    else:
        str_list.remove("#")
        "".join(str_list)
    return (strings_with_symbol(str_list)
            if '#' in str_list
            else "".join(str_list))


assert strings_with_symbol("a#bc#d") == "bd"
assert strings_with_symbol("abc#d##c") == "ac"
assert strings_with_symbol("abc##d######") == ""
assert strings_with_symbol("#######") == ""
assert strings_with_symbol("") == ""


# Свечи
# Когда свеча догорает, остается остаток. Остатки можно объединить, чтобы
# создать новую свечу, которая при догорании, в свою очередь, оставит еще один
# остаток. У вас есть количество свечей. Какое общее количество свечей вы
# можете сжечь, если предположить, что вы создадите новые свечи, как только у
# вас останется достаточно остатков?

# Пример Если у Вас 5(candles_number) свечей, и из 2х(make_new) остатков вы
# можете сделать 1 новую свечу, то ответе будет: 9.

# По шагам, чтобы сжечь 9 свечей:

# сожгите 5 свечей, получите 5 остатков;
# создайте еще 2 свечи, используя 4 остатка (остался 1);
# сожгите 2 свечи, в итоге останется 3 остатка;
# создайте еще одну свечу, используя 2 остатка (остался 1);
# сожгите созданную свечу, что даст еще один остаток (всего 2 остатка);
# создать свечу из оставшихся остатков;
# зажгите последнюю свечу.
# Таким образом, можно сжечь 5+2+1+1=9 свечей, что и является ответом.


def burn_candles(can_do, make_new, candles_burned=0):
    """This function updates amount of burned candles based on amount of newly
       created ones

    can_do: amount of candles we possibly can do
    make_new: number of candles needed to make a new one
    candles_burned: how much candles have been burned before function call

    return: updated amount of burned candles
    """
    candles_burned += can_do * make_new
    return candles_burned


def count_leftovers(leftovers, can_do, make_new):
    """This function counts amount of leftovers after new candles creation
       and burning

    leftovers: amount of candle leftovers
    can_do: amount of candles made before
    make_new: number of candles needed to make a new one

    return: updated amount of leftovers
    """
    leftovers = can_do + (leftovers % make_new)
    return leftovers


def solution(candles_number, make_new):
    """This function counts amount of candles need to be burned based on
       the ability to make new candles from leftovers

    candles_number: initial amount of candles
    make_new: amount of candles needed to make a new one

    return: amount of candles need to be burned
    """
    candles_burned = 0
    leftovers = candles_number
    while leftovers >= make_new:
        can_do = leftovers // make_new
        candles_burned = burn_candles(can_do, make_new, candles_burned)
        leftovers = count_leftovers(leftovers, can_do, make_new)
    candles_burned += leftovers
    return candles_burned


assert solution(5, 2) == 9
assert solution(1, 2) == 1
assert solution(15, 5) == 18
assert solution(12, 2) == 23
assert solution(6, 4) == 7
assert solution(13, 5) == 16
assert solution(2, 3) == 2

# Подсчет количества букв
# На вход подается строка, например, "cccbba" результат работы программы -
# строка “c3b2a"

# Примеры для проверки работоспособности:

# "cccbba" == "c3b2a"
# "abeehhhhhccced" == "abe2h5c3ed"
# "aaabbceedd" == "a3b2ce2d2"
# "abcde" == "abcde"
# "aaabbdefffff" == "a3b2def5"


def count_letters(input_string):
    """This function counts letters in string

    input_string: input string

    return: string with counted letters
    """
    result = ""
    for el, group in groupby(input_string):
        result += f'{el}{len(list(group))}'.replace('1', "")
    return result


assert count_letters("cccbba") == "c3b2a"
assert count_letters("abeehhhhhccced") == "abe2h5c3ed"
assert count_letters("aaabbceedd") == "a3b2ce2d2"
assert count_letters("abcde") == "abcde"
assert count_letters("aaabbdefffff") == "a3b2def5"
