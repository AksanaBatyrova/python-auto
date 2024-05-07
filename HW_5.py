"""
1. Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
2. Напишите программу, которая добавляет 'ing' к словам
3. B строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
4. Напишите программу которая удаляет пробел в начале, в конце строки
5. Имена собственные всегда начинаются c заглавной буквы, за которой следуют строчные буквы.
Исправьте данное имя собственное так, чтобы оно соответствовало этому утверждению.
"pARiS" >> "Paris"

"""


# Task 1

TASK1_STRING = 'www.my_site.com#about'

# Function replacing two symbols within one string
def replace_symbols(string, symbol_1, symbol_2):
    return string.replace(symbol_1, symbol_2)

print(replace_symbols(TASK1_STRING, '#', '/'))


# Task 2

# Function adding ending 'ing' to string
def add_ing(string):
    return string + 'ing'

print(add_ing("point"))


# Task 3

TASK3_STRING = 'Ivanou Ivan'

# Function that can swap the words within one string
def swap_the_words(string):
    string = string.split()[::-1]
    string = " ".join(string)
    return string

print(swap_the_words(TASK3_STRING))


# Task 4

# Function that can remove spaces from the start and the end of the string
def remove_spaces(string):
    return string.strip()

print(remove_spaces("  word  "))


# Task 5

TASK5_STRING = 'pARiS'

# Function that changes the case of the string to lowercase with first capital letter
def change_case(string):
    return string.capitalize()

print(change_case(TASK5_STRING))
