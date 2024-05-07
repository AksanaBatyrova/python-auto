"""
1. Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
2. Напишите программу, которая добавляет 'ing' к словам
3. B строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
4. Напишите программу которая удаляет пробел в начале, в конце строки
5. Имена собственные всегда начинаются c заглавной буквы, за которой следуют строчные буквы. 
Исправьте данное имя собственное так, чтобы оно соответствовало этому утверждению. "pARiS" >> "Paris"

"""


# Task 1

task1_string = 'www.my_site.com#about'

def replace_symbols(string, symbol_1, symbol_2):
    return string.replace(symbol_1, symbol_2)

print(replace_symbols(task1_string, '#', '/'))


# Task 2

def add_ing(word):
    return word + 'ing'

print(add_ing("point"))


# Task 3

task3_string = 'Ivanou Ivan'

def swap_the_words(string):
    string = string.split()[::-1]
    string = " ".join(string)
    return string

print(swap_the_words(task3_string))


# Task 4

def remove_spaces(string):
    return string.strip()

print(remove_spaces("  word  "))


# Task 5

task5_string = 'pARiS'

def change_case(string):
    return string.capitalize()

print(change_case(task5_string))
