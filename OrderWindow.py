from tkinter import *
import time
import random

def order(table_number):
  
  print("The table number is : ", table_number)
  # later!!
  # join_table_number = ""
  # for items in table_number : join_table_number += ''+items
  # print("The joined table number : ", join_table_number,'\n',type(join_table_number) )
  root = Tk()
  root.geometry("640x480")
  root.title("Order Section")
  
  for i in range(5):
    ct = [random.randrange(256) for x in range(3)]
    brightness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114*ct[2]))
    ct_hex = "%02x%02x%02x" % tuple(ct)
    bg_color = '#' + "".join(ct_hex)
    l = Label(root, 
                  text=table_number[i], 
                  fg='White' if brightness < 120 else 'Black', 
                  bg=bg_color)
    l.place(x = 20, y = 30 + i*30, width=120, height=25)

  root.mainloop()