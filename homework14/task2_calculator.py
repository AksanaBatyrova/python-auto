"""Homework 14. Task 2 Engineer evaluate_expression"""

# Инженерный калькулятор
# Напишите программу - инженерный калькулятор. Передусмотрите возможные ошибки
# и обработайте их. ~ - это предложение ввода.

# Базовые требования:
# Программа считает простые математические выражения:
# ~ 5 + 49

# Программа ожидает от пользователя ввода математического выражения и
# правильно его трактует:
# ~ 10 - 3 + 18
# ~ 2 ** 3 - 17

import operator


def prepare_expression(expression):
    """This function prepares entered expression to future calculations"""
    expression = expression.replace('**', '^').replace(' ', '')

    tokens = []

    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            j = i
            while j < len(expression) and expression[j].isdigit():
                j += 1
            tokens.append(int(expression[i:j]))
            i = j
        elif expression[i] in '+-*/^':
            tokens.append(expression[i])
            i += 1
        else:
            raise ValueError(f"Unknown token: {expression[i]}")

    return tokens


def eval_operator(tokens, sign_op):
    """This function calculate mathematic expressions and handling errors"""
    processed = []

    i = 0
    while i < len(tokens):
        if tokens[i] in sign_op:
            if i in (0, len(tokens)-1):
                raise ValueError("Invalid expression")

            if processed[-1] in sign_op:
                raise ValueError("Invalid expression")

            if tokens[i + 1] in sign_op:
                raise ValueError("Invalid expression")

            op = sign_op[tokens[i]]
            processed[-1] = op(processed[-1], tokens[i + 1])
            i += 2
        else:
            processed.append(tokens[i])
            i += 1
    return processed


def calculator(expression):
    """This function returns calculation results"""
    tokens = prepare_expression(expression)

    tokens = eval_operator(tokens, {'^': operator.pow})
    tokens = eval_operator(tokens, {'*': operator.mul, '/': operator.truediv})
    tokens = eval_operator(tokens, {'+': operator.add, '-': operator.sub})

    return tokens[0]


assert calculator('5 + 49') == 54
assert calculator('10 - 3 + 18') == 25
assert calculator('2 ** 3 - 17') == -9
