from tkinter import *
import time
import OrderWindow

def system():

    root = Tk()
    root.geometry("640x480")
    root.title("Restaurant Management Tool")

    # Topframe
    topframe = Frame(root, bg="grey", width=640, height=100)
    topframe.pack(side=TOP)

    # centerframe
    centframe = Frame(root, bg="lime", width=640, height=250)
    centframe.pack(side=TOP, anchor=CENTER)

    # Time
    localtime = time.asctime(time.localtime(time.time()))
    # Top part
    main_lbl = Label(topframe, font=('Baskerville', 35, 'bold'), text="Welcome to Lance's\nRestaurant Management System", fg="Blue",
                   anchor=W)
    main_lbl.grid(row=0, column=0)
    main_lbl = Label(topframe, font=('Bodoni', 15,), text=localtime, fg="grey", anchor=W)
    main_lbl.grid(row=1, column=0)

    blank_lbl1 = Label(centframe, font=('ariel', 12, 'bold'), text="  ", fg="Blue",
                   anchor=CENTER)
    blank_lbl1.grid(row=0, column=2)
    blank_lbl2 = Label(centframe, font=('ariel', 12, 'bold'), text="  ", fg="Blue",
                   anchor=CENTER)
    blank_lbl2.grid(row=1, column=2)
    # instruction to the user label
    inst_lbl = Label(centframe, font=('ariel', 12, 'bold'), text="Please enter the Table number to proceed", fg="Blue",
                   anchor=CENTER)
    inst_lbl.grid(row=2, column=2)

    # Entry box
    name_var = StringVar
    name_entry = Entry(centframe,textvariable = name_var, font=('calibre',10,'normal'))
    name_entry.grid(row=3, column=2)
    
        # Action on button function
    def actionBtn(tblno):
      OrderWindow.system(tblno)
      root.destroy()



    # Proceed button
    p_btn=Button(centframe,text = 'Go!', command = lambda: actionBtn(name_var), anchor=CENTER)
    p_btn.grid(row=4, column=2)
    


    root.mainloop()