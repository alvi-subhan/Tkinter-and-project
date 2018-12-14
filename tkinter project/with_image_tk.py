from tkinter import *
from tkinter.messagebox import showinfo

root=Tk()
root.geometry("700x400")
root.title("Landing page")

name=StringVar()
email=StringVar()

#name=name.get()
#email=email.get()

def home_popup():
    showinfo("Pop-up", "You are already on Home page!")

def gov():
    win=Toplevel(root)
    win.title("Government jobs")
    win.geometry("400x300")
    M=Label(win,text="Following are the jobs in Government sector",fg="Black").grid(sticky=W)
    sp=Label(win,text=" ").grid(row=1)
    Button(win,text="National highway jobs",command=apply).grid(sticky=W)
    Button(win,text="Motorway jobs",command=apply).grid(sticky=W)
    Button(win,text="Police Patrolling",command=apply).grid(sticky=W)

def private():
    win=Toplevel(root)
    win.title("Private jobs")
    win.geometry("600x300")
    M=Label(win,text="Following are the jobs in Private sector",fg="Black").grid(sticky=W)
    sp=Label(win,text=" ").grid(row=1)
    Button(win,text="Senior Accountant",command=apply).grid(sticky=W)
    Button(win,text="Python Developer",command=apply).grid(sticky=W)
    Button(win,text="Data Analyst",command=apply).grid(sticky=W)

def police_1():
    win=Toplevel(root)
    win.title("Police jobs")
    win.geometry("400x300")
    M=Label(win,text="Following are the jobs in Police ",fg="Black").grid(sticky=W)
    sp=Label(win,text=" ").grid(row=1)
    Button(win,text="Police Patrolling",command=apply).grid(sticky=W)

def apply():
    global win_apply
    win_apply=Toplevel(root)
    win_apply.geometry("700x400")
    win_apply.title("Application window")

    lab=Label(win_apply,text="Please enter your name and email address").grid()
    name_1=Label(win_apply,text="Name").grid(row=3)
    email_1=Label(win_apply,text="Email").grid(row=4)

    name_entry=Entry(win_apply,textvariable=name).grid(row=3,column=1)
    email_entry=Entry(win_apply,textvariable=email).grid(row=4,column=1)

    check=Checkbutton(win_apply,text="Subscribe the newsletter of Jobsalert.pk").grid(columnspan=2)
    apply_button=Button(win_apply,text="Apply",command=name_email_get).grid()
    cancel_button=Button(win_apply,text="Cancel",command=win_apply.destroy).grid()
    

def name_email_get():
    nm=name.get()+" Thank you for applying, we will get back to you shortly."
    em=email.get()
    error="You can't apply without mentioning your name or email"
    if name.get() and email.get():
        l1=Message(win_apply,text=nm).grid()
    else:
        l2=Message(win_apply,text=error).grid()
    
def no_jobs():
    win=Toplevel(root)
    win.title("No jobs")
    win.geometry("350x200")
    l1=Message(win,text="We currently don't have job listing in this category,leave us your email address to get notified").grid()
    spacer=Label(root,text=" ").grid(row=1) #using this to add a space between l1 and l2
    l2=Label(win,text="Email").grid(row=2)
    E1=Entry(win).grid(row=2,column=1)

    submit=Button(win,text="Submit",command=win.destroy).grid()


img=PhotoImage(file="/home/subhan-alvi/Desktop/tkinter/logo.png")
job_pk=Label(root,text="JOBSALERT.PK",image=img)
#job_pk=Label(root,text="JOBSALERT.PK",font="verdana")
job_pk.grid(column=0,columnspan=3,sticky=W)


#b1=Button(f_top,text="quit",command=quit)
#b1.grid(row=0,column=8)

#space between frame and toolbar
sp=Label(root,text=" ").grid(row=1)

#tool bar
home=Button(root,text="Home",bg="white",fg="black",command=home_popup).grid(row=2,column=2)
Govt=Button(root,text="Government",bg="white",fg="black",command=gov).grid(row=2,column=3)
privt=Button(root,text="Private",bg="white",fg="black",command=private).grid(row=2,column=4,sticky=W)
fed=Button(root,text="Fed Govt",bg="white",fg="black",command=no_jobs).grid(row=2,column=5,sticky=W)
navy=Button(root,text="Navy",bg="white",fg="black",command=no_jobs).grid(row=2,column=6,sticky=W)
army=Button(root,text="Army",bg="white",fg="black",command=no_jobs).grid(row=2,column=7,sticky=W)
police=Button(root,text="Police",bg="white",fg="black",command=police_1).grid(row=2,column=8,sticky=W)

#frame for jobs
#job_frame=Frame(root)

#list of jobs
sp=Label(root,text=" ").grid(row=3)
job1=Button(root,text="National highway jobs",command=apply).grid(sticky=W)
job2=Button(root,text="Motorway jobs",command=apply).grid(sticky=W)
job3=Button(root,text="Nursing jobs",command=apply).grid(sticky=W)
job4=Button(root,text="Police Patrolling",command=apply).grid(sticky=W)
job5=Button(root,text="Senior Accountant",command=apply).grid(sticky=W)
job6=Button(root,text="Python Developer",command=apply).grid(sticky=W)
job7=Button(root,text="Data Analyst",command=apply).grid(sticky=W)


root.mainloop()