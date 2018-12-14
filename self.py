from tkinter import *
win=Tk()
lab=Label(win,text="hello")
#win.title("made it mysel")
lab.pack(side=RIGHT)
top=Frame(win)
top.pack()
bottom_frame=Frame(win)
bottom_frame.pack(side=BOTTOM)

b1=Button(top,text="button 1",fg='red')
b1.pack(side=LEFT)

b3=Button(top,text="button 3",fg='red')
b3.pack()


b2=Button(bottom_frame,text="button 2",fg='yellow',command=quit)
b2.pack()


win.mainloop()
