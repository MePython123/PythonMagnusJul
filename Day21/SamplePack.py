from tkinter import *
root = Tk()
root.geometry('200x200')

lb = Button(root,text="Left",height=5,width=5,fg="green")
lb.pack(side=LEFT)
rb = Button(root,text="Right",height=5,width=5,fg="purple")
rb.pack(side=RIGHT)
tb = Button(root,text="Top",height=5,width=5,fg="red")
tb.pack(side=TOP)
bb = Button(root,text="Bottom",height=5,width=5,fg="blue")
bb.pack(side=BOTTOM)


root.mainloop()