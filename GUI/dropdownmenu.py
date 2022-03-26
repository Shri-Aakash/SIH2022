from tkinter import *
#from tkinter import ttk
import os
#import subprocess
global root
root=Tk()
global clicked
clicked=StringVar()

def selected(event):
    #myLabel=Label(root, text=clicked.get()).pack()
    if clicked.get()=='Navigation':
        myLabel=Label(root, text="Now initiating Navigation").pack()
        os.system(r'"C:\Program Files\VideoLAN\VLC\vlc.exe"')
    elif clicked.get()=="Schedule setting":
        myLabel=Label(root, text="Now initiating Schedule setting").pack()
        os.system(r'"C:\Program Files\Microsoft Office\root\Office16\WINWORD.exe"')
    elif clicked.get()=="Medicine dispenser":
        myLabel=Label(root, text="Now initiating Medicine dispenser").pack()
        os.system(r'"C:\WINDOWS\system32\notepad.exe"')
    elif clicked.get()=="Threat Alarm":
        myLabel=Label(root, text="Now initiating Threat Alarm").pack()
        os.system(r'"C:\WINDOWS\system32\SnippingTool.exe"')


def Menu_page():
    root.title('Behaviour Page')
    root.geometry('500x500')
    options=[
    "Navigation",
    "Schedule setting",
    "Medicine dispenser",
    "Threat Alarm"
    ]

    clicked.set(options[2])
    drop=OptionMenu(root,clicked,*options,command=selected)
    drop.pack(pady=20)


    #myButton=Button(root,text="Open Program",command=selected)
    #myButton.pack(pady=20)
    root.mainloop()