from tkinter import *
import item_menu as im
# import time
# import random
from tkinter import messagebox
import order as od

def order(table_number, item_number, item_price, item_name):

  #aList = []
  
  print("The table number is : ", table_number)
  # later!!
  # join_table_number = ""
  # for items in table_number : join_table_number += ''+items
  # print("The joined table number : ", join_table_number,'\n',type(join_table_number) )
  root = Tk()
  root.geometry("440x280")
  root.title("Order Section")


  root.config(bg="lime")

  # Create left and right frames
  left_frame = Frame(root, width=200, height=400, bg='grey')
  left_frame.grid(row=0, column=0, padx=10, pady=5)

  # Create frames 
  Label(left_frame, text="***Order Details***").grid(row=0, column=1, padx=5, pady=5)

  
  Label(left_frame, text="Table Number").grid(row=1, column=0, padx=5, pady=5)
  Label(left_frame, text=table_number, relief=RIDGE, width=15).grid(row=1,column=1)
  
  
  def on_click():
    v1 = int(e.get())
    print("The value entered was ", v1)
    total = "$ "+str(float(round(item_price*v1) * 1.12))
    t.config(text=total)

    # for items in quan_var.get(): aList.append(items)
    # print(aList)
    #return NameError

  # def callback():
  #   var1 = "Value Changed!"
  #   #print("Value Changed")
  #   Label(left_frame, text=label_list[4], relief=RIDGE, width=15).grid(row=6,column=0)
  #   Label(left_frame, text=var1, relief=RIDGE, width=15).grid(row=6,column=1)

  # def print_entry(var):
  #     print(var.get())
  
  
  def checkOut():
    item_quantity = int(e.get())
    total = "$ "+str(int(round(item_price * item_quantity) * 1.12))
    txt = "You Ordered\nItem Name - {}\nQuantity - {}\nTax - 12%\nTotal Pay : {}\n\n Thanks for your order!".format(item_name, item_quantity,total )
    messagebox.showinfo("SidLabs", txt)
    order = od.Orders(table_number, item_name, item_price, item_quantity,1.12)
    order.storeOrderToCsv()
    messagebox.showinfo("SidLabs", "Database Updated!")
    
  
  label_list = ['Item No.','Price','Quantity','Tax','Total ->']
  Label(left_frame, text=label_list[0], relief=RIDGE, width=15).grid(row=2,column=0)
  Label(left_frame, text=item_number, relief=RIDGE, width=15).grid(row=2,column=1)
  
  # Price Label
  Label(left_frame, text=label_list[1], relief=RIDGE, width=15).grid(row=3,column=0)
  Label(left_frame, text=item_price, relief=RIDGE, width=15).grid(row=3,column=1)

  #Quantity Label
  #Create an variable to store the user-input
  #quan_var = StringVar()
  
  #quan_var.trace("w", callback)

  Label(left_frame, text=label_list[2], relief=RIDGE, width=15).grid(row=4,column=0)
  
  e = Entry(left_frame, bg='grey', relief=RIDGE, width=10)
  e.grid(row=4,column=1)
  


  # Tax label
  Label(left_frame, text=label_list[3], relief=RIDGE, width=15).grid(row=5,column=0)
  Label(left_frame, text='12%', relief=RIDGE, width=15).grid(row=5,column=1)

  # Grand Total
  Label(left_frame, text=label_list[4], relief=RIDGE, width=15).grid(row=6,column=0)
  t = Label(left_frame, text='total', relief=RIDGE, width=15)
  t.grid(row=6,column=1)

  Button(left_frame, text="add", command= on_click).grid(row=7,column=0)
  Button(left_frame, text="Checkout", command=checkOut).grid(row=7,column=1)
  
  
  root.mainloop()

