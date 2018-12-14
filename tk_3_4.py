from tkinter import *

win=Tk()
win.geometry("200x100")

l1=Label(win,text="name",fg="black",bg="yellow")
l2=Label(win,text="email",fg="pink",bg="black")

e1=Entry(win)
e2=Entry(win)

check=Checkbutton(win,text="please tick me")

l1.grid(row=0,sticky=E)
l2.grid(row=1,sticky=E)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

check.grid(columnspan=2,sticky=SW)

win.mainloop()
