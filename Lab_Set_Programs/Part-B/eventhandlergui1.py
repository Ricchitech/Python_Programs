#Creating a GUI using a class
#click counter
#demonstrate binding an event with an event handler
import tkinter
from tkinter import *

class Application(tkinter.Frame):
#GUI application which displays number of button clicks
#class application extending frame (Application object that holds all the button)
#GUI application which counts button clicks

    def __init__(self, master):
        """ Initialize the frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0 #the number of button clicks
        self.create_widget()

    def create_widget(self):
        """ Create button which displays number of clicks. """
        self.bttn = Button(self)
        self.bttn["text"] = "Total Clicks: 0"
        self.bttn["command"] = self.update_count
        self.bttn.grid()
    
    def update_count(self):
        """ Update number of clicks and display new total. """
        self.bttn_clicks += 1
        self.bttn["text"] = "Total Clicks: " + str(self.bttn_clicks)


#main
root =Tk()
root.title("Click Counter")
root.geometry("400x200")
app=Application(root)
root.mainloop()