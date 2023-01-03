from tkinter import *
import item_menu as im
# import time
# import random

def order(table_number, item_number, item_price):
  
  print("The table number is : ", table_number)
  # later!!
  # join_table_number = ""
  # for items in table_number : join_table_number += ''+items
  # print("The joined table number : ", join_table_number,'\n',type(join_table_number) )
  root = Tk()
  root.geometry("640x480")
  root.title("Order Section")

  root.config(bg="skyblue")

  # Create left and right frames
  left_frame = Frame(root, width=200, height=400, bg='grey')
  left_frame.grid(row=0, column=0, padx=10, pady=5)

  right_frame = Frame(root, width=400, height=480, bg='lightgreen')
  right_frame.grid(row=0, column=1, padx=10, pady=5)

  # Create frames 
  Label(left_frame, text="***Order Details***").grid(row=0, column=1, padx=5, pady=5)

  
  Label(left_frame, text="Table Number").grid(row=1, column=0, padx=5, pady=5)
  Label(left_frame, text=table_number, relief=RIDGE, width=15).grid(row=1,column=1)

  Label(right_frame, text="***Cart***").grid(row=0,column=0, padx=5, pady=5)

  #image = PhotoImage(file="menu-card.jpg")
  #original_image = image.subsample(3,3)  # resize image using subsample

  def on_click():
    im.items()
    root.destroy()
  
  label_list = ['Item No.','Price','Quantity','Tax','Total ->']
  Label(left_frame, text=label_list[0], relief=RIDGE, width=15).grid(row=2,column=0)
  Label(left_frame, text=item_number, relief=RIDGE, width=15).grid(row=2,column=1)
  
  Label(left_frame, text=label_list[1], relief=RIDGE, width=15).grid(row=3,column=0)
  Label(left_frame, text=item_price, relief=RIDGE, width=15).grid(row=3,column=1)

  Label(left_frame, text=label_list[2], relief=RIDGE, width=15).grid(row=4,column=0)
  Entry(left_frame, bg='grey', relief=RIDGE, width=10).grid(row=4,column=1)

  Label(left_frame, text=label_list[3], relief=RIDGE, width=15).grid(row=5,column=0)
  Label(left_frame, text='12%', relief=RIDGE, width=15).grid(row=5,column=1)

  Label(left_frame, text=label_list[4], relief=RIDGE, width=15).grid(row=6,column=0)
  Label(left_frame, text='total', relief=RIDGE, width=15).grid(row=6,column=1)

  Button(left_frame, text="Menu", command= on_click).grid(row=7,column=0)
  Button(left_frame, text="Add to cart", command='#').grid(row=7,column=1)
  
  
  root.mainloop()

