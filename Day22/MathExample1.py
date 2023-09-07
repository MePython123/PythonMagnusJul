from tkinter import *
from tkinter import messagebox
from functools import partial
root = Tk()
root.geometry('250x250')

def m1(lbResult,n1,n2):
    num1 = n1.get()
    num2 = n2.get()
    result = num1+num2
    lbResult.config(text="Result = %d" %result)
    return

n1=IntVar()
n2=IntVar()

lb1 = Label(root,text="Num1").grid(row=1,column=0)
lb2 = Label(root,text="Num2").grid(row=2,column=0)
lbResult = Label(root)
lbResult.grid(row=8,column=2)

e1 = Entry(root,textvariable=n1).grid(row=1,column=2)
e2 = Entry(root,textvariable=n2).grid(row=2,column=2)

m1 = partial(m1,lbResult,n1,n2)
b1 = Button(root,text="Calculate",command=m1).grid(row=3,column=0)

root.mainloop()