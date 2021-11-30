from tkinter import *
root= Tk()
v=IntVar()
Radiobutton(root,text='CSA',variable=v,value=1).pack(anchor=W)
Radiobutton(root,text='C&IT',variable=v,value=2).pack(anchor=W)
root.mainloop()