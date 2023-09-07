from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('250x250')
v1 = StringVar()

def m1():
    select = "Selected Option is "+v1.get()
    lb1.config(text=select)

r1 = Radiobutton(root,text="Male",variable=v1, value="Male",command=m1)
r2 = Radiobutton(root,text="Female",variable=v1, value="Female",command=m1)
r3 = Radiobutton(root,text="Others",variable=v1, value="Others",command=m1)
r1.pack()
r2.pack()
r3.pack()

lb1 = Label(root)
lb1.pack()

root.mainloop()