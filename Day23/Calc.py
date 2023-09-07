from tkinter import *

root = Tk()
root.geometry("300x260")
root.resizable(0,0)
root.title("Calculator")

def btn_click(value):
    global data
    data=data+str(value)
    itext.set(data)

def btn_clear():
    global data
    data=""
    itext.set(data)

def btn_equals():
    global data
    result = str(eval(data))
    itext.set(result)

data=""
itext=StringVar()

#Creating a Separate Frame for the Text Box
inputFrame = Frame(root,bg='grey',width=300,height=50)
inputFrame.pack(side=TOP)

# Text Box for the Data Insertion
inputText = Entry(inputFrame,textvariable=itext,width=48,font=('Calibri',20,'bold'),justify=RIGHT)
inputText.grid(row=0,column=0)
inputText.pack()

# Creating a separate frame for the buttons
btnsFrame = Frame(root,bg='green',width=300, height=210)
btnsFrame.pack()

# Calculator Buttons Creation
seven = Button(btnsFrame,text="7",width=9,height=3,command=lambda :btn_click(7)).grid(row=1,column=0)
eight = Button(btnsFrame,text="8",width=9,height=3,command=lambda :btn_click(8)).grid(row=1,column=1)
nine = Button(btnsFrame,text="9",width=9,height=3,command=lambda :btn_click(9)).grid(row=1,column=2)
plus = Button(btnsFrame,text="+",width=9,height=3,command=lambda :btn_click("+")).grid(row=1,column=3)

four = Button(btnsFrame,text="4",width=9,height=3,command=lambda :btn_click(4)).grid(row=2,column=0)
five = Button(btnsFrame,text="5",width=9,height=3,command=lambda :btn_click(5)).grid(row=2,column=1)
six = Button(btnsFrame,text="6",width=9,height=3,command=lambda :btn_click(6)).grid(row=2,column=2)
sub = Button(btnsFrame,text="-",width=9,height=3,command=lambda :btn_click("-")).grid(row=2,column=3)

one = Button(btnsFrame,text="1",width=9,height=3,command=lambda :btn_click(1)).grid(row=3,column=0)
two = Button(btnsFrame,text="2",width=9,height=3,command=lambda :btn_click(2)).grid(row=3,column=1)
three = Button(btnsFrame,text="3",width=9,height=3,command=lambda :btn_click(3)).grid(row=3,column=2)
multi = Button(btnsFrame,text="*",width=9,height=3,command=lambda :btn_click("*")).grid(row=3,column=3)

clear = Button(btnsFrame,text="C",width=9,height=3,command=lambda :btn_clear()).grid(row=4,column=0)
zero = Button(btnsFrame,text="0",width=9,height=3,command=lambda :btn_click(0)).grid(row=4,column=1)
equals = Button(btnsFrame,text="=",width=9,height=3,command=lambda :btn_equals()).grid(row=4,column=2)
div = Button(btnsFrame,text="/",width=9,height=3,command=lambda :btn_click("/")).grid(row=4,column=3)

root.mainloop()