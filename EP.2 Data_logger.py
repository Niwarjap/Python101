from tkinter import *
from tkinter import ttk
from tkinter import messagebox

Gui = Tk()
Gui.title('Data Logger')
Gui.geometry('500x400')
Gui.resizable(height=FALSE,width=FALSE)


L1 = Label(Gui,text='Welcome',font=('OCR A Extended',20))
L1.place(x=200, y=30)

################
def Butt1():
    nameg = E1.get()
    snameg = E2.get()
    messagebox.showinfo('Successful!',f'Name : {nameg}\n\nSurname : {snameg}\n\nAdded!')

def clear_text():
   E1.delete(0,END)
   E2.delete(0,END)

def EXIT():
    Gui.destroy()

################

FB1 = Frame(Gui)
FB1.place(x=80, y=280)

FB3 = Frame(Gui)
FB3.place(x=200, y=280)

FB4 = Frame(Gui)
FB4.place(x=320, y=280)

FLB1 = LabelFrame(Gui,text='Name')
FLB1.place(x=145, y=100)

FLB2 = LabelFrame(Gui,text='Surname')
FLB2.place(x=145, y=180)

##################

B1 = ttk.Button(FB1,text='Submit',command=Butt1)
B1.pack(ipadx=20, ipady=5)

B3 = ttk.Button(FB3,text='Clear',command=clear_text)
B3.pack(ipadx=20, ipady=5)

B4 = ttk.Button(FB4,text='Exit',command=EXIT)
B4.pack(ipadx=20, ipady=5)

E1 =ttk.Entry(FLB1)
E1.pack(ipadx=50, ipady=5)

E2 =ttk.Entry(FLB2)
E2.pack(ipadx=50, ipady=5)


Gui.mainloop()


