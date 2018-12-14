from tkinter import *

root=Tk()
#w1=Toplevel(root)

def create():
    window=Toplevel(root)
    b1=Button(window,text="hello",command=quit)
    b1.pack()

    M=Message(window,text="hello this is a msg",fg="red")
    M.pack()
b=Button(root,text="create window",command=create)
b.pack()


root.mainloop()