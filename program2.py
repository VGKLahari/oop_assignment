from tkinter import *
from PIL import ImageTk,Image
import time
def usc():
    global win2
    f=open('details.py','r')
    i=len(f.readlines())
    f.seek(0)
    for t in range(0,i+1):
        k=list(f.readline().split(','))
        if(k[0]==e1.get() and k[1]==e2.get()):
            win2=Tk()
            win2.state('zoomed')
            win2.config(bg='#ffdddd')
            break
    if(t==i):
        l3=Label(text='invalid password or user name')
        l3.place(relx=0.43,rely=0.85)
    f.close()
def lsc():
    global win2
    f=open('details.py','a')
    f.write(e3.get()+','+e4.get()+','+e5.get()+'\n')
    win2=Tk()
    win2.state('zoomed')
    win2.config(bg='#ffdddd') 
def sign_in():
    global e3,e4,e5
    name=Label(text='NAME',font=('Courier',10),bg='#B7E9F7')
    name.place(relx=0.35,rely=0.65)
    pw=Label(text='PASSWORD',font=('Courier',10),bg='#B7E9F7')
    pw.place(relx=0.35,rely=0.70)
    e3=Entry()
    e3.place(relx=0.53,rely=0.65)
    e4=Entry(show='*')
    e4.place(relx=0.53,rely=0.70)
    pno=Label(text='PHONE NUMBER',font=('Courier',10),bg='#B7E9F7')
    pno.place(relx=0.35,rely=0.75)
    e5=Entry()
    e5.place(relx=0.53,rely=0.75)
    b4=Button(text='enter',command=lsc)
    b4.place(relx=0.53,rely=0.80)
def log_in():
    global e1,e2,b3,l2
    name=Label(text='NAME',font=('Courier',10),bg='#B7E9F7')
    name.place(relx=0.35,rely=0.65)
    pw=Label(text='PASSWORD',font=('Courier',10),bg='#B7E9F7')
    pw.place(relx=0.35,rely=0.70)
    e1=Entry()
    e1.place(relx=0.53,rely=0.65)
    e2=Entry(show='*')
    e2.place(relx=0.53,rely=0.70)
    b3=Button(text='enter',command=usc,bg='#B7E9F7')
    b3.place(relx=0.53,rely=0.80)
def f1():
    global l1,win1,b1,b2,p2
    l1.destroy()
    p2=ImageTk.PhotoImage(Image.open('logpage.jpg'))
    l2=Label(image=p2)
    l2.place(relx=0.25,rely=0)
    b1=Button(text='sign up',height=2,width=15,bg='#B7E9F7',command=sign_in)
    b2=Button(text='log in',height=2,width=15,command=log_in,bg='#B7E9F7')
    b1.place(relx=0.35,rely=0.55)
    b2.place(relx=0.53,rely=0.55)
win1=Tk()
win1.state('zoomed')
p1=ImageTk.PhotoImage(Image.open('l1.png'))
l1=Label(image=p1)
l1.grid()
win1.after(3000,f1)
win1.config(bg='#ffdddd')
#-------------------------------------------------------------homepage----------
def ss():
    global kk,c,win2,l4,l5,l6,l7
    if(c==4):
        c=0
        kk[3].grid_forget()
        kk[0].grid()
    else:
        kk[c-1].grid_forget()
        kk[c].grid()
    c=c+1
    win2.after(2000,ss)    

k1=Label(image=l4,master=win2)
k2=Label(image=l5,master=win2)
k3=Label(image=l6,master=win2)
k4=Label(image=l7,master=win2)
kk=[k1,k2,k3,k4]
#bb=Button(text='hii')
#bb.grid(row=1,column=0)
#bb.config(bg='#FF00FF')
c=1
k1.grid()
win2.after(2000,ss)
















