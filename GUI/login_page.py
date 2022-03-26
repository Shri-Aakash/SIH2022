from tkinter import *
from tkinter import messagebox
import os
import dropdownmenu

def login():
    username=entry1.get()
    password=entry2.get()
    if(username=='' and password==''):
        messagebox.showinfo("","Blank Not Allowed")
    elif(username=="Sigma" and password=="admin1234"):
        messagebox.showinfo("","login success")
        dropdownmenu.Menu_page()
    else:
        messagebox.showinfo("","incorrect username and password")


w=Tk()
w.geometry('350x500')
w.title("Login")


global entry1
global entry2
Label(w,text="Username").place(x=20,y=20)
Label(w,text="Password").place(x=20,y=70)

entry1=Entry(w,bd=5)
entry1.place(x=140,y=20)

entry2=Entry(w,bd=5)
entry2.place(x=140,y=70)

Button(w,text="Login",command=login,height=3,width=13,bd=6).place(x=100,y=100)
w.mainloop()
