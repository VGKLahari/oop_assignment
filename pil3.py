from tkinter import *
from PIL import ImageTk,Image
import random
k=Tk()
k.state("zoomed")
i1=Image.open("white.jpg")
itk1=ImageTk.PhotoImage(i1)
l1=Label(image=itk1)
l1.place(relx=0,rely=0)
i2=Image.open("hair1.jpg")
itk2=ImageTk.PhotoImage(i2)
l2=Label(image=itk2)
l2.place(x=718,y=382)
p1=i1.load()
p2=i2.load()
i3=Image.open("hair1.jpg")
itk3=ImageTk.PhotoImage(i3)
l3=Label(image=itk3);i=0
'''
def x():
      global i,l1,itk1,p2,k,l2,itk2
      if(i==10):
            k.destroy()
            return 0
      print(i)
      l1.destroy();l2.destroy()
      p1[10*i,10*i]=(0,0,0)
      itk1=ImageTk.PhotoImage(i1)
      l1=Label(image=itk1)
      p2[10*i,10*i]=(255,255,255)
      
      itk2=ImageTk.PhotoImage(i2)
      l2=Label(image=itk2)
      
      l1.place(x=0,y=0)
      
      l2.place(x=718,y=382)
      
      i=i+1
      k.after(2000,x)
k.after(2000,x)'''


i=0

z=0
list1=[]
for i in range(0,100):
  
    for j in range(0,100):
      list1.append([i,j])
length=len(list1)
def a():
      
          global i,k,p1,p2,i2,i1,l1,itk2,itk1,l1,l2,list1,length
          if(len(list1)==0):
                  return 0
          
                  
          l1.destroy();l2.destroy()
          temp=random.choice(list1)
          r,g,b=p2[temp[0],temp[1]]
          p2[temp[0],temp[1]]=(255,255,255)
          p1[random.randint(768,850),random.randint(300,420)]=(r,g,b)
          list1.remove(temp)
          itk1=ImageTk.PhotoImage(i1)
          l1=Label(image=itk1)
          itk2=ImageTk.PhotoImage(i2)
          l2=Label(image=itk2)
          '''for j in range(0,i2.size[0]):
              
              r,g,b=p2[j,i]
              p2[j,i]=(255,255,255)
              p1[718+(i*j)+5,382-(i*i)-5]=(r,g,b)
              
              
              itk1=ImageTk.PhotoImage(i1)
              l1=Label(image=itk1)
              itk2=ImageTk.PhotoImage(i2)
              l2=Label(image=itk2)'''
          
          l1.place(x=0,y=0)
              
          l2.place(x=718,y=382)
              #l3.place(x=0,y=0)
              #k.after(250,y)
          
          
          #i=i+1
          k.after(5,a)
     
k.after(500,a)

        
