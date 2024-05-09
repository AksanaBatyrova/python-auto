"""
1. Перевести строку в список "Robin Singh" => ["Robin”, “Singh"]
2. "I love arrays they are my favorite" =>
   ["I", "love", "arrays", "they", "are", "my", "favorite"]
3. Дан список: [Ivan, Ivanou], и 2 строки: Minsk, Belarus
   Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
4. Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
   сделайте из него строку => "I love arrays they are my favorite"
5. Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
   удалите элемент из списка под индексом 6
"""

# Task 1
TASK1_STRING = "Robin Singh"
print(list(TASK1_STRING.split(" ")))


# Task 2
TASK2_STRING = "I love arrays they are my favorite"
print(list(TASK2_STRING.split(" ")))


# Task 3
Name_Surname = ['Ivan', 'Ivanou']
CITY = 'Minsk'
COUNTRY = 'Belarus'
print(f"Привет, {' '.join(Name_Surname)}! "
      f"Добро пожаловать в {CITY} {COUNTRY}!")


# Task 4
task4_string = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(' '.join(task4_string))

# Task 5
arr = ['Apple', 'Orange', 'Pear', 'Cherry', 'Banana', 'Mango', 'Grapes', 'Lime',
      'Strawberry', 'Blackcurrant']
arr[2] = 'Plum'
del arr[6]
print(arr)
