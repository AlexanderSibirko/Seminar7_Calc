from fractions import Fraction

# left_value = input()
# oper = input()
# right_value = input()

x = Fraction(int(left_value[0: left_value.index('/')]),
             int(left_value[left_value.index('/')+1:len(left_value)]))

y = Fraction(int(right_value[0: right_value.index('/')]),
             int(right_value[right_value.index('/')+1: len(right_value)]))


def r_calc_block(left_value, oper, right_value):
    if oper == '+':
        res = r_sum()
    if oper == '-':
        res = r_sub(left_value, right_value)
    if oper == '*':
        res = r_mult()
    if oper == '/':
        res = r_div()
    return res


def r_sub():
    return x-y


def r_mult():
    return x * y


def r_div():
    return x / y


def r_sum():
    return x + y


# print(r_sum(), r_sub(), r_div(), r_mult())
# print(r_calc_block(left_value, oper, right_value))
