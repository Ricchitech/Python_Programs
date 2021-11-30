import tkinter as tk
r=tk.Tk()
r.title("Button Demonstration")
button=tk.Button(r,text="Click Me", width=25,command=r.destroy)
button.pack()
r.mainloop()