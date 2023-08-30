from tkinter import *
root = Tk()
root.geometry('250x250')

username = Label(root,text="Username").grid(row=0,column=0)
t1 = Entry(root).grid(row=0,column=1)
password = Label(root,text="Password").grid(row=2,column=0)
t2 = Entry(root).grid(row=2,column=1)
b1 = Button(root,text="Login").grid(row=4,column=1)

root.mainloop()