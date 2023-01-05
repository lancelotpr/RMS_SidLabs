from tkinter import *
import time
import item_menu as im

aList = []

root = Tk()

def login():

# setup and initiate screen    
  root.geometry("640x480")
  root.title("Restaurant Management Tool")
  root.configure(bg="lime")
    # Action on button function
  
  def actionBtn():
    print_entry(name_var)
    for items in name_var.get(): aList.append(items)
   
    im.items()
    
    global root
    root.destroy()
    root.quit() # not working!

    import sys; sys.exit()  
  
  name_var = StringVar()
  def print_entry(var):
      print(var.get())

  
  
  # top frame
  top_frame = Frame(root, bg="grey", width=640, height=100)
  
  # center frame
  center_frame = Frame(root, bg="white", width=640, height=250)
  
  # Time
  localtime = time.asctime(time.localtime(time.time()))

  # Main label
  main_lbl = Label(top_frame, font=('Baskerville', 35, 'bold'), text="Welcome to Lance's\nRestaurant Management login", fg="Blue",
                  anchor=W)
  
  # time label
  local_time = Label(top_frame, font=('Bodoni', 15,), text=localtime, fg="grey", anchor=W)
  
  # a blank label 
  blank_lbl1 = Label(center_frame, font=('ariel', 12, 'bold'), text="  ", fg="Blue",
                  anchor=CENTER)
  
  # another blank label 
  blank_lbl2 = Label(center_frame, font=('ariel', 12, 'bold'), text="  ", fg="Blue",
                  anchor=CENTER)
  
  # instruction to the user label
  inst_lbl = Label(center_frame, font=('ariel', 12, 'bold'), text="Please enter the Table number to proceed", fg="Blue",
                  anchor=CENTER)
  
  # Entry box
  #name_var = StringVar(center_frame, value = "table number")
  name_entry = Entry(center_frame,textvariable = name_var, font=('calibre',10,'normal'))
  #newInt = name_var.get()
  #for items in name_var.get() : print(items)
  #name_entry.register(validate_table())
  
  

  # Go! button
  p_btn=Button(center_frame,text = 'Go!', command = lambda: actionBtn(), anchor=CENTER)
  
  
  # Organize stuff on the grid 
  top_frame.pack(side=TOP)
  center_frame.pack(side=TOP, anchor=CENTER)
  
  #name_entry.pack(side=BOTTOM, anchor=CENTER)
  main_lbl.grid(row=0, column=0)
  local_time.grid(row=1, column=0)
  blank_lbl1.grid(row=0, column=2)
  blank_lbl2.grid(row=1, column=2)

  blank_lbl1.grid(row=1, column=2)
  blank_lbl2.grid(row=2, column=2)

  inst_lbl.grid(row=3, column=2)
  blank_lbl1.grid(row=4, column=2)
  name_entry.grid(row=5, column=2)
  blank_lbl1.grid(row=6, column=2)
  p_btn.grid(row=7, column=2)
  
  root.mainloop()
