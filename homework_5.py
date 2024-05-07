"""
1. Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
2. Напишите программу, которая добавляет 'ing' к словам
3. B строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
4. Напишите программу которая удаляет пробел в начале, в конце строки
5. Имена собственные всегда начинаются c заглавной буквы, за которой
   следуют строчные буквы. Исправьте данное имя собственное так, 
   чтобы оно соответствовало этому 
   утверждению. "pARiS" >> "Paris"
"""


# Task 1
TASK1_STRING = 'www.my_site.com#about'
print(TASK1_STRING.replace( '#', '/'))


# Task 2
TASK2_STRING = 'point'
print(TASK2_STRING + 'ing')


# Task 3
TASK3_STRING = 'Ivanou Ivan'
TASK3_STRING = TASK3_STRING.split()[::-1]
TASK3_STRING = " ".join(TASK3_STRING)
print(TASK3_STRING)


# Task 4
TASK4_STRING = '  word  '
print(TASK4_STRING.strip())


# Task 5
TASK5_STRING = 'pARiS'
print(TASK5_STRING.capitalize())
