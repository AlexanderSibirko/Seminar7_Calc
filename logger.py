from datetime import datetime as dt
from time import time


def result_logger(left_value, oper, right_value,data):
  data_str = f'{str(left_value)} {oper} {str(right_value)}'
  time = dt.now().strftime('%H:%M')
  print('{}; операция : {} результат : {}\n'.format(time, data_str, data))
  with open('log.csv', 'a', encoding = 'UTF-8') as file:
    file.write('{}; операция : {} результат :{}\n'.format(time, data_str, data))
    
   

# def pressure_logger(data):
#     time = dt.now().strftime('%H:%M')
#     with open('log.csv', 'w') as file:
#         file.write('{};pressure;{}\n'
#                     .format(time, data))
   

# def wind_speed_logger(data):
#     time = dt.now().strftime('%H:%M')
#     with open('log.csv', 'w') as file:
#         file.write('{};wind_speed;{}\n'
#                     .format(time, data))

