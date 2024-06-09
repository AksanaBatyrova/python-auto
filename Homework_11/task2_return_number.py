"""Homework 11 Decorators, Task 2: Return number"""

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
