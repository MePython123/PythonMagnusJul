from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('200x2000')

def m1():
    text = "You have Clicked the Button"
    messagebox.showinfo("Message",text)

#b1 = Button(root,text="Click",command=m1) # displays text in m1
b1 = Button(root,text="Click",command=root.destroy) # It closes entire window if you click

b1.pack()

root.mainloop()