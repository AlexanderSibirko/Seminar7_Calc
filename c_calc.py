# модуль для расчетов операций с комплексными числами

import cmath

def Calc_block(left_value, oper, right_value):
    if oper == '+':
        res = sum(left_value, right_value)
    if oper == '-':
        res = sub(left_value, right_value)
    if oper == '*':
        res = mult(left_value, right_value)
    if oper =='/':
        res = div(left_value, right_value)
    return res


def sum(left_value: complex, right_value: complex):
    return left_value + right_value


def sub(left_value: complex, right_value: complex):
    return left_value - right_value


def mult(left_value: complex, right_value: complex):
    return left_value * right_value


def div(left_value: complex, right_value: complex):
    return left_value / right_value
