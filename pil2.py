from tkinter import *
from PIL import ImageTk,Image
import time
k=Tk()
k.state("zoomed")
img =Image.open("meh3.jpg")
p=img.size[1]

ll=[]
for i in range(0,img.size[1]):
    ll.append([])
    ll[i].append(1);ll[i].append(1);ll[i].append(1)
    j=0;i=0
while(i<img.size[1]):
    ll[i][0]=img.crop((0,i,p,i+1))
    ll[i][1]=ImageTk.PhotoImage(ll[i][0])
    ll[i][2]=Label(k,image=ll[i][1])
    ll[i][2].place(x=100,y=(j+60)*2.5)
    j=j+1
    i=i+1
'''ll[2][2].place(x=0,y=11)
ll[3][2].place(x=0,y=4)
ll[4][2].place(x=0,y=5)
ll[5][2].place(x=0,y=6)
ll[6][2].place(x=0,y=7)
ll[7][2].place(x=0,y=8)
ll[8][2].place(x=0,y=9)
ll[9][2].place(x=0,y=10)
ll[10][2].place(x=0,y=11)'''

t=[];s=[]
for i in range(0,401):
    t.append([]);s.append([])
    t[i]=ll[0][0].crop((i,0,i+1,1))
    s[i]=Label(image=ImageTk.PhotoImage(t[i]))
def xp():
    s[i].place(x=101+i+6,y=60+i+8)

for i in range(0,401):
     
     s[i].place(x=101+i+2,y=60+i+2)
     k.after(5000,xp)
     
