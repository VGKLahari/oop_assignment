from tkinter import *
from PIL import ImageTk,Image
a=10
def y():
    global p,l,k
    if(a==10):
        k=Toplevel()
        p=ImageTk.PhotoImage(Image.open("bride2.png"))
        #k.title('hello')
        #k.state("zoomed")
        #p=ImageTk.PhotoImage(Image.open("bride2.png"))
        l=Button(k,image=p)
        l.pack()
    pass
def x():
    global k
    y()
t=Tk()
t.title("hi")
t.after(3000,x)
'''k=Tk()
p=ImageTk.PhotoImage(Image.open("bride2.png"))
l=Button(k,image=p)
l.pack()
'''
t.mainloop()
