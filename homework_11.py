"""This module is a homework 11 Decorators"""

# Положительные аргументы функции
# Напишите декоратор @validate_arguments, который проверяет, что все аргументы
# функции являются положительными числами. Если встречается аргумент, не
# соответствующий этому условию, функция должна вывести сообщение об ошибке.

# Вот некоторые подсказки:
# Внутри декоратора, используйте цикл for для перебора аргументов функции.
# Используйте оператор if для проверки, является ли аргумент положительным
# числом.
# Если аргумент не соответствует условию, используйте оператор raise для
# вызова исключения ValueError.


def positive_arguments(function):
    """This decorator function return ValueError if function argument is
       not a positive number

    function: function to check arguments of which

    return: function that check arguments for type and positivity
    """
    def check_args(*args):
        for arg in args:
            if not isinstance(arg, (int, float)) or arg <= 0:
                raise ValueError(f'{arg} is not a positive number')
        return function(*args)
    return check_args


@positive_arguments
def example_function(*args):
    """This function sum all arguments it takes"""
    return sum(args)


example_function(5, -4)

# Вернуть число
# Создайте декоратор, который проверяет, является ли результат функции числом
# и выводит сообщение об ошибке, если это не так. Вот некоторые подсказки:

# Внутри декоратора, после вызова функции, проверьте тип результата с помощью
# функции isinstance().
# Если тип не является числом, выведите сообщение об ошибке с помощью функции
# print().


def is_a_number(function):
    """This decorator function print message if function result is not a number

    function: function to check arguments of which

    return: function that check arguments for type
    """
    def check_function_result():
        result = function()
        if not isinstance(result, (int, float)):
            return f'{result} is not a number'
        return function()
    return check_function_result


@is_a_number
def return_number():
    """This function return number 5"""
    return 5


@is_a_number
def return_string():
    """This function return string 'a'"""
    return 'a'


assert return_number() == 5
assert return_string() == 'a is not a number'

# Декоратор типов
# Напишите декоратор, который проверял бы тип параметров функции,
# конвертировал их если надо и складывал:


def typed(data_type):
    """This decorator function checks the input function arguments,
       converts them to int if needed and and sum

    function: function to check arguments of which
    arg_type: type all arguments needs to be converted to

    return: function that check arguments for type
    """
    def convert(function):
        def wrapper(*args):
            args = (data_type(arg) for arg in args)
            return function(*args)
        return wrapper
    return convert


@typed(data_type=str)
def add(a, b):
    """This function sum all arguments it takes"""
    return a + b


assert add("3", 5) == "35"
assert add(5, 5) == "55"
assert add('a', 'b') == 'ab'


@typed(data_type=int)
def add2(a, b, c):
    """This function sum all arguments it takes"""
    return a + b + c


assert add2(5, 6, 7) == 18


@typed(data_type=float)
def add3(a, b, c):
    """This function sum all arguments it takes"""
    return a + b + c


assert add3(0.1, 0.2, 0.4) == 0.7000000000000001

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
