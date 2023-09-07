from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('250x250')
v1=IntVar()
v2=IntVar()
v3=IntVar()

cb1 = Checkbutton(root,text="Mango",variable=v1,onvalue=1,offvalue=0,height=3,width=10)
cb2 = Checkbutton(root,text="Orange",variable=v2,onvalue=1,offvalue=0,height=3,width=10)
cb3 = Checkbutton(root,text="Apple",variable=v3,onvalue=1,offvalue=0,height=3,width=10)
cb1.pack()
cb2.pack()
cb3.pack()

root.mainloop()