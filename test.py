from datetime import datetime as dt
from time import time
import tkinter as tk

a = input("Enter real value: ")
for i in a:
  if i in "0123456789.-":
    continue
  else: a = a.replace(i,'')
b = input("Enter imaginary value: ")
for i in b:
  if i in "0123456789.-":
    continue
  else: b = b.replace(i,'')
z1 = complex(eval(a),eval(b))
z2 = complex(eval(b),eval(a))
res = z1/z2

window = tk.Tk()
greeting = tk.Label(text='{}; a : {} b : {} результат : {}\n'.format(time,a, b, res),width=100,height=20)
greeting.pack()
label = tk.Label(text="Имя")
entry = tk.Entry()
label.pack()
entry.pack()
window.mainloop()
  
