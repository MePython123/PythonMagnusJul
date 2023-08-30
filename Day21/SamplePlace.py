from tkinter import *
root = Tk()
root.geometry('250x250')

username = Label(root,text="Username").place(x=30,y=50)
t1 = Entry(root).place(x=100,y=50)
password = Label(root,text="Password").place(x=30,y=100)
t2 = Entry(root).place(x=100,y=100)
b1 = Button(root,text="Login").place(x=30,y=150)

root.mainloop()