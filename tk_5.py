from tkinter import *
win=Tk()

win.geometry("200x100")

def fun():
    print("hi theere")

b1=Button(win,text="add function",command=fun,fg="yellow",bg="black")
b1.pack()

win.mainloop()
