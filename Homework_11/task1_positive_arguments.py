"""Homework 11 Decorators, Task 1: Positive Arguments"""

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
                raise ValueError
        return function(*args)
    return check_args


@positive_arguments
def example_function(*args):
    """This function sum all arguments it takes"""
    return sum(args)


def both_positive(a, b):
    """This function handle the Value Error exception"""
    try:
        return example_function(a, b)
    except ValueError:
        return 'Invalid argument: not a positive number'


assert (both_positive(5, -4)) == 'Invalid argument: not a positive number'
