"""Homework 11 Decorators, Task 3: Type decorator"""

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
