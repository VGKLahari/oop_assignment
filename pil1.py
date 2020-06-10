from tkinter import *
from PIL import Image,ImageTk
import time
k=Tk();i=0
def x():
    global pixels,img,ii,l,i,k
       # for every col:
    for j in range(img.size[0]):    # For every row
        pixels[i,j] = (255,0,255) # set the colour accordingly
    l.destroy()
    img.save("g6.jpg")
    ii=ImageTk.PhotoImage(img)
    l=Label(k,image=ii)
    l.grid(row=0,column=0)
    i=i+1
    if(i<=img.size[1]):
        k.after(250,x)
    else:
        pass
img =Image.open("g6.jpg")
pixels=img.load()
ii=ImageTk.PhotoImage(img)
l=Label(k,image=ii)
l.grid(row=0,column=0)

k.after(2000,x)
