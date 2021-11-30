from tkinter import *
import tkinter

top=Tk()
mb=Menubutton(top,text="Condiments",relief=RAISED)
mb.grid()
mb.menu=Menu(mb,tearoff=0)
mb["menu"]=mb.menu

mayoVar=IntVar()
ketchVar=IntVar()
mb.menu.add_checkbutton(label="Mayo",variable=mayoVar)
mb.menu.add_checkbutton(label="Ketchup",variable=ketchVar)
mb.menu.add_checkbutton(label="Sauce", variable=ketchVar)
mb.pack()
top.mainloop()
