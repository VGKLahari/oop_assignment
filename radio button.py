from tkinter import *
from PIL import ImageTk,Image
def x():
    print(v.get())
    if(v.get()==100):
        print("hello")
def b():
    print('hi')
k=Tk()
i=ImageTk.PhotoImage(Image.open('bride1.jpg'))
v=IntVar()
r=Checkbutton(image=i,command=x,var=v,offvalue=0,onvalue=100)

a=Checkbutton(text='ho',command=b)
b=Checkbutton(text='ho',command=b)
r.pack()
a.pack()
b.pack()
try:
        for i in range(temmp,len(V)):
            if(V[i].get()!=0):
                sums=sums+i.get()
except:
        temmp=i+1
        bill()
