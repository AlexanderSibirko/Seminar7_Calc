from c_calc import Calc_block as c_calc
# import console_ui
from logger import result_logger as write_log

a, op, b = console_ui.ask_user()
# a = float('5')
# op = '+'
# b = 3
res = c_calc(a,op,b)
write_log(a,op,b,res)