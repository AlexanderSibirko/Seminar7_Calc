from c_calc import Calc_block as c_calc
from logger import result_logger as write_log
import data_transformation as d_t
import console_ui as c_ui


def button_click():
    j = d_t.data_formatting(c_ui.input_data())
    c_ui.view_data(c_calc(j), 'Ответ:')
    write_log(j, c_calc(j))


button_click()

# c-ui.view_data(c_calc.Calc_block(in_d())

# a = 6
# op = '-'
# b = 50
# res = c_calc(a,op,b)
# write_log(a,op,b,res)


# a = 6 + 2j
# op = '+'
# b = 50
# res = c_calc(a,op,b)
# write_log(a,op,b,res)


# a = 65+ 2j
# op = '/'
# b = 0
# res = c_calc(a, op, b)
# write_log(a, op, b, res)
