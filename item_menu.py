from tkinter import *
# import time
# import random
import LoginWindow as lw
import order as od
import OrderWindow as odw

def tableNumber():
  var1 = ""
  for elements in lw.aList : var1 += elements
  return var1


def regOrder (tableNumber, itemName, itemPrice, itemQuantity, tax):

  order1 = od.Orders(tableNumber, itemName, itemPrice, itemQuantity, tax)

  order1.storeOrderToCsv()

def items():
  
  root = Tk()
  root.geometry("640x480")
  root.title("Item's Menu")

  item_dict = {"Pizza" : ["P101", 2.5],
              "Burger" : ["B101", 3], 
              "Pasta" : ["P102", 5],
              "Coke" : ["C101", 1.5],
             }

  # Create Frame widget
  left_frame = Frame(root, width=400, height=450)
  left_frame.grid(row=0, column=0, padx=10, pady=5)

  # Create frame within left_frame
  item_holder = Frame(left_frame, width=350, height=350, bg="purple")
  item_holder.grid(row=3, column=0, padx=5, pady=5)

  
  # Create label above the item_holder
  Label(left_frame, text="Item List").grid(row=1, column=0, padx=5, pady=5)

  l0 = []

  def sel1():
    print("sel1 was called!")
    l1 = ['Pizza',"P101", 2.5]
    l0.append(l1)
    
  def sel2():
    print("sel2 was called!")
    l2 = ['Burger',"B101", 3]
    l0.append(l2)
    
  def sel3():
    print("sel3 was called!")
    l3 = ["Pasta", "P102", 5]
    l0.append(l3)
    
  def sel4():
    print("sel4 was called!")
    l4 = ['Coke',"C101", 1.5]
    l0.append(l4)
    

  def proceed():
    var1 = tableNumber()
    for items in l0: print("Items :", items)
    print("Table No : ", var1)
    odw.order(var1)
    print("Proceed was called ->")





  Label(item_holder, text='Name', fg='black',relief=RIDGE, width=15).grid(row=0,column=0)
  Label(item_holder, text='Code', fg='black',relief=RIDGE, width=15).grid(row=0,column=1)
  Label(item_holder, text='Price', fg='black',relief=RIDGE, width=15).grid(row=0,column=2)
  Label(item_holder, text='Select', fg='black',relief=RIDGE, width=15).grid(row=0,column=3)


  r = 1
  var = StringVar()
  for keys in item_dict.keys():
    Label(item_holder, text=keys, fg='grey',relief=RIDGE, width=15).grid(row=r,column=0)
    r += 1

  txt1 = '$'+str(item_dict['Pizza'][1])
  Label(item_holder, text=item_dict['Pizza'][0], fg='grey',relief=RIDGE, width=15).grid(row=1,column=1)
  Label(item_holder, text=txt1, fg='grey',relief=RIDGE, width=15).grid(row=1,column=2)
  Radiobutton(item_holder, bg='grey',text="Select Item", variable=var, value=0,
              command=sel1).grid(row=1,column=3)


  txt2 = '$'+str(item_dict['Burger'][1])
  Label(item_holder, text=item_dict['Burger'][0], fg='grey',relief=RIDGE, width=15).grid(row=2,column=1)
  Label(item_holder, text=txt2, fg='grey',relief=RIDGE, width=15).grid(row=2,column=2)
  Radiobutton(item_holder, bg='grey',text="Select Item", variable=var, value=1,
               command=sel2).grid(row=2,column=3)

  txt3 = '$'+str(item_dict['Pasta'][1])
  Label(item_holder, text=item_dict['Pasta'][0], fg='grey',relief=RIDGE, width=15).grid(row=3,column=1)
  Label(item_holder, text=txt3, fg='grey',relief=RIDGE, width=15).grid(row=3,column=2)
  Radiobutton(item_holder, bg='grey',text="Select Item", variable=var, value=1,
               command=sel3).grid(row=3,column=3)

  txt4 = '$'+str(item_dict['Coke'][1])
  Label(item_holder, text=item_dict['Coke'][0], fg='grey',relief=RIDGE, width=15).grid(row=4,column=1)
  Label(item_holder, text=txt4, fg='grey',relief=RIDGE, width=15).grid(row=4,column=2)
  Radiobutton(item_holder, bg='grey',text="Select Item", variable=var, value=1,
               command=sel4).grid(row=4,column=3)
  

  
  # button 
  Button(item_holder, text= "Order!", command=proceed).grid(row=10, column=2)

  root.mainloop()

