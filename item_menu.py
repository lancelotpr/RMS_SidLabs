from tkinter import *
# import time
# import random

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


  def sel():
    print("sel was called!")

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
              command=sel).grid(row=1,column=3)


  txt2 = '$'+str(item_dict['Burger'][1])
  Label(item_holder, text=item_dict['Burger'][0], fg='grey',relief=RIDGE, width=15).grid(row=2,column=1)
  Label(item_holder, text=txt2, fg='grey',relief=RIDGE, width=15).grid(row=2,column=2)
  Radiobutton(item_holder, bg='grey',text="Select Item", variable=var, value=1,
              command=sel).grid(row=2,column=3)
  

   

  root.mainloop()
