# новый модуль
from datetime import datetime as dt
from time import time


def oper_logger(left_value, oper, right_value):
  data_str = f'{str(left_value)} {oper} {str(right_value)}'
  time = dt.now().strftime('%H:%M')
  # 
  with open('log.csv', 'a', encoding = 'UTF-8') as file:
    file.write('{}; операция : {} \n'.format(time, data_str))
# 
def res_logger(data):
  time = dt.now().strftime('%H:%M')
  print('{}; результат : {}\n'.format(time, data))
  with open('log.csv', 'a', encoding = 'UTF-8') as file:
    file.write('{}; результат :{}\n'.format(time, data))
    
 

