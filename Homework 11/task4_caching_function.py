
"""Homework 11 Decorators, Task *: Caching function"""

# Функция кэширования *
# Напишите декоратор @cache, который кэширует результаты вызова функции и
# возвращает закэшированное значение при повторных вызовах с теми же
# аргументами. Это поможет избежать повторных вычислений для одинаковых
# входных данных и ускорит работу программы.

# Подсказки:

# Используйте словарь для хранения закэшированных значений. Ключом словаря
# будет набор аргументов функции, а значением - результат вызова функции с
# этими аргументами.
# Внутри декоратора, передайте аргументы функции в качестве ключа для доступа
# к закэшированным значениям.
# Если ключ уже есть в словаре, верните соответствующее значение. Если ключа
# нет, вызовите функцию, сохраните результат в словаре и верните его.
# Пример использования:


def cache(function):
    """This decorator function adds argument and function result to the
       dictionary for future retrieving

    function: function to apply decorator on

    return: function that adds argument and function result to the dictionary
    """
    cache_dict = {}

    def wrapper(arg):
        if arg in cache_dict:
            return cache_dict[arg]
        cache_dict[arg] = function(arg)
        return function(arg)
    return wrapper


@cache
def fibonacci(n):
    """This function implements functionality for counting fibonacci
       sequence
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


assert fibonacci(5) == 5
assert fibonacci(10) == 55
assert fibonacci(5) == 5
