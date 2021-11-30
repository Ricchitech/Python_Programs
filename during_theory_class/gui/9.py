from tkinter import *
main= Tk()
ourMessage='This is our message'
messageVar=Message(main,text=ourMessage)
messageVar.config(bg='lightgreen',font=('times',24,'italic'))
messageVar.pack()
main.mainloop()