from c_calc import Calc_block as c_calc
from logger import result_logger as write_log
import data_transformation as d_t
import console_ui as c_ui


def button_click():
    j = d_t.data_formatting(c_ui.input_data())
    c_ui.view_data(c_calc(j), 'Ответ:')
    write_log(j, c_calc(j))


button_click()
