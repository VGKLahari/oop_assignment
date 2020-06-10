from tkinter import *
from PIL import ImageTk,Image
count=0;ti='hi';temmp=0;V=[];sums=0;BILL=[];fcount=0
add=r"C:\Users\Lahari\Desktop\oop assignment"
C1=0;C2=0;C3=0;C4=0;C5=0;C6=0;T=0
import mysql.connector

def confirm(para):
    global BILL,V,CB1,CB2,CB3,CB4,CB5
    if(para==1):
        CB1.config(state=DISABLED)
    elif(para==2):
        CB2.config(state=DISABLED)
    elif(para==3):
         CB3.config(state=DISABLED)
    elif(para==4):
         CB4.config(state=DISABLED)
    elif(para==5):
         CB5.config(state=DISABLED)
    for i in V:
        if(i.get()!=0):
            BILL.append(i.get())
    
    
def bdetails():
    global f2,fd,ti,fcount
    
    if(len(BE1.get())==0 or len(BE2.get())==0 or len(BE3.get("1.0","end-1c"))==0 or len(BE4.get())==0 or len(BE5.get())==0 or (BE5.get()).isnumeric()==False):
        nl=Label(win4,text="Please enter the details properly",bg="#ffdddd",fg="black")
        nl.place(relx=0.45,rely=0.55)
    else:
        
        f2=open(add+r"\new.py","a+")
        f2.write(BE4.get()+','+BE5.get()+','+BE1.get()+','+BE2.get()+','+BE3.get("1.0","end-1c")+','+sums+','+ti+","+'\n')
        f2.close()
        F=open(add+r"\count.py","r+")
        fcount=int(F.read())
        F.seek(0)
        fd=open(add+r"\bdetails.py","r")
        listd=fd.readlines();length=len(listd)
        f=list(listd[fcount].split(','))
        fcount=fcount+1
        F.write(str(fcount))
        dl1=Label(win4,text="Your beautician details\nName:"+f[0]+'\n'+"Phonenumber:"+f[1],font=("Consolas",15),bg="#ffdddd",fg="#0000FF")
        dl1.place(relx=0.42,rely=0.7)
        
def back(wins):
    global count
    count=count+1
    wins.iconify()
def bill():
    
    global win4,T1,count,Bill,BE1,BE2,BE3,BE4,BE5,Bu,sums,temmp,V,BILL
    try:
        for i in BILL:
            sums=sums+i
    except:
        pass

    sums='RS '+str(sums)
    win4=Toplevel()
    win4.state("zoomed")
    win4.config(bg="#ffdddd")
    Tl=Label(win4,text='Thank you for using Hormoso',bg='#FFC8FB',fg='#0000FF',font=("Consolas",60))                 
    Tl.place(relx=0.1,rely=0.050)
    Bill=Label(win4,text="Your total bill is "+sums,bg='#FFC8FB',fg='#0000FF',font=("Consolas",20))                 
    Bill.place(relx=0.37,rely=0.18)
    BE4=Entry(win4);BE5=Entry(win4)
    BE1=Entry(win4);BE2=Entry(win4);BE3=Text(win4,height=5,width=30);L1=Label(win4,text='Date:',bg='#FFC8FB',font=("Arial",12));L2=Label(win4,text='Timings:',bg='#FFC8FB',font=("Arial",12))
    L3=Label(win4,text='Address:',bg='#FFC8FB',font=("Arial",12));L4=Label(win4,text='Name:',bg='#FFC8FB',font=("Arial",12));L5=Label(win4,text='Phone no:',bg='#FFC8FB',font=("Arial",12))
    L1.place(relx=0.4,rely=0.35);L2.place(relx=0.4,rely=0.4);L3.place(relx=0.4,rely=0.45),L5.place(relx=0.4,rely=0.3);L4.place(relx=0.4,rely=0.25)
    BE1.place(relx=0.55,rely=0.35);BE2.place(relx=0.55,rely=0.4);BE3.place(relx=0.55,rely=0.45);BE5.place(relx=0.55,rely=0.3);BE4.place(relx=0.55,rely=0.25)
    Bu=Button(win4,text='Enter',bg='#B7E9F7',font=("Arial",12),command=bdetails)
    Bu.place(relx=0.475,rely=0.6)
    count=count+1
def nailart():
    global x1,x2,x3,x4,x5,e1,e2,e3,e4,e5,b1,b2,b3,b4,b5,D2,D3,D4,D5,D6,pay,V,D1,F1,F2,F3,F4,F5,ti,BILL,win3,count,C1,CB1,WIN3
    ti="nailart"
    A=lambda t=1:confirm(t);Z=lambda :back(WIN3)
    if(C1==0):
        WIN3=Toplevel()
        WIN3.state('zoomed')
        WIN3.config(bg="#ffdddd")
        Dl=Label(WIN3,text='Nail Art',bg='#ffdddd',fg='#0000FF',font=("Consolas",60))                 
        Dl.place(relx=0.3,rely=0.050)
        x1=ImageTk.PhotoImage(Image.open(add+r"\Stensil.jpg"))
        x2=ImageTk.PhotoImage(Image.open(add+r"\Air brush.jpg"))
        x3=ImageTk.PhotoImage(Image.open(add+r"\foot.jpg"))
        x4=ImageTk.PhotoImage(Image.open(add+r"\simple.jpg"))
        x5=ImageTk.PhotoImage(Image.open(add+r"\stylish.jpg"))
        e1=IntVar();e2=IntVar();e3=IntVar();e4=IntVar();e5=IntVar()
        b1=Checkbutton(WIN3,image=x1,var=e1,onvalue=175,bg="#FFC8FB")
        b2=Checkbutton(WIN3,image=x2,var=e2,onvalue=250,bg="#FFC8FB")
        b3=Checkbutton(WIN3,image=x3,var=e3,onvalue=150,bg="#FFC8FB")
        b4=Checkbutton(WIN3,image=x4,var=e4,onvalue=200,bg="#FFC8FB")
        b5=Checkbutton(WIN3,image=x5,var=e5,onvalue=300,bg="#FFC8FB")
        b1.place(relx=0.1,rely=0.2);b2.place(relx=0.1,rely=0.32);b3.place(relx=0.1,rely=0.44);b4.place(relx=0.1,rely=0.56);b5.place(relx=0.1,rely=0.68)
        D2=Label(WIN3,text='Stensil',bg='#ffdddd',fg='black',font=("Calibri",20));D3=Label(WIN3,text='Air brush',bg='#ffdddd',fg='black',font=("Calibri",20))
        D4=Label(WIN3,text='Foot',bg='#ffdddd',fg='black',font=("Calibri",20));D5=Label(WIN3,text='Simple',bg='#ffdddd',fg='black',font=("Calibri",20))
        D6=Label(WIN3,text='Stylish',bg='#ffdddd',fg='black',font=("Calibri",20))
        D2.place(relx=0.25,rely=0.2);D3.place(relx=0.25,rely=0.32);D4.place(relx=0.25,rely=0.44);D5.place(relx=0.25,rely=0.56);D6.place(relx=0.25,rely=0.68)
        F1=Label(WIN3,text='Rs 175',bg='#ffdddd',fg='black',font=("Calibri",20));F2=Label(WIN3,text='Rs 250',bg='#ffdddd',fg='black',font=("Calibri",20))
        F3=Label(WIN3,text='Rs 150',bg='#ffdddd',fg='black',font=("Calibri",20));F4=Label(WIN3,text='Rs 200',bg='#ffdddd',fg='black',font=("Calibri",20))
        F5=Label(WIN3,text='Rs 300',bg='#ffdddd',fg='black',font=("Calibri",20))
        F1.place(relx=0.5,rely=0.2);F2.place(relx=0.5,rely=0.32);F3.place(relx=0.5,rely=0.44);F4.place(relx=0.5,rely=0.56);F5.place(relx=0.5,rely=0.68)
        pay=Button(WIN3,text="Proceed to pay bill",command=bill,font=("Arial",20),bg="#B7E9F7")
        pay.place(relx=0.68,rely=0.5)
        V=[e1,e2,e3,e4,e5]
        BB1=Button(WIN3,text="back",command=Z,font=("Arial",20),bg="#B7E9F7")
        BB1.place(relx=0.68,rely=0.65)
        
        CB1=Button(WIN3,text="confirm",command=A,font=("Arial",20),bg="#B7E9F7")
        CB1.place(relx=0.68,rely=0.75)
        
       
    else:
        WIN3.deiconify()
        
    C1=C1+1
def bridal():
    global i1,tt,i2,tt1,i3,tt2,i4,tt3,i5,tt4,i6,tt5,var,var1,var2,var3,var4,V,ti,BILL,win3,count,C2,CB2,WIN4
    ti="bridal"
    B=lambda t=2:confirm(t);Z1=lambda :back(WIN4)
    if(C2==0):
        i2=ImageTk.PhotoImage(Image.open(add+r"\bridal4.jpg"))
        i3=ImageTk.PhotoImage(Image.open(add+r"\UrbanClap.jpg"))
        i4=ImageTk.PhotoImage(Image.open(add+r"\bridal2.jpg"))
        i5=ImageTk.PhotoImage(Image.open(add+r"\bridal.jpg"))
        i6=ImageTk.PhotoImage(Image.open(add+r"\bridal3.jpg"))
        var=IntVar()
        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        WIN4=Toplevel()
        WIN4.state('zoomed')
        WIN4.config(bg='#ffdddd')
        h1=Label(WIN4,text='Bridal Packages',bg='#ffdddd',font=('consolas',25))
        h1.place(relx=0.35,rely=0)
        r1=Checkbutton(WIN4,text=' Traditional Bridal Makeup \n price:20,000 for one time draping,makeup and hairstyling',variable=var,onvalue=20000,offvalue=0,bg='#ffdddd',fg='#0000FF',font=('consolas',15))
        tt1=Label(WIN4,image=i2)
        tt2=Label(WIN4,image=i3)
        tt3=Label(WIN4,image=i4)
        tt4=Label(WIN4,image=i5)
        tt5=Label(WIN4,image=i6)
        tt1.place(relx=0.59,rely=0.1)
        tt2.place(relx=0.62,rely=0.25)
        tt3.place(relx=0.62,rely=0.4)
        tt4.place(relx=0.62,rely=0.57)
        tt5.place(relx=0.62,rely=0.74)
        r1.place(relx=0,rely=0.1)
        r2=Checkbutton(WIN4,text='Reception Bridal Package \n price:18,000 for draping sarees in different styles,hairstyling,makeup',variable=var1,onvalue=18000,offvalue=0,bg='#ffdddd',fg='#0000FF',font=('consolas',15))
        r2.place(relx=0,rely=0.25)
        r3=Checkbutton(WIN4,text='Airbrush Bridal Makeup \n price:22,000 for draping sarees in different styles,hairstyling \n airbrush makeup(flawless finish,light-weight makeup)',variable=var2,onvalue=22000,offvalue=0,bg='#ffdddd',fg='#0000FF',font=('consolas',15))
        r3.place(relx=0,rely=0.4)
        r4=Checkbutton(WIN4,text='Mineral Bridal Makeup \n price:23,000 for draping sarees in different styles,hairstyling \n mineral makeup(natural,flawless finish,chemical-free composition)',variable=var3,onvalue=23000,offvalue=0,bg='#ffdddd',fg='#0000FF',font=('consolas',15))
        r4.place(relx=0,rely=0.57)
        r5=Checkbutton(WIN4,text='Muslim Bridal Makeup \n price:19,000 for  one time draping ,hairstyling , makeup',variable=var4,onvalue=19000,offvalue=0,bg='#ffdddd',fg='#0000FF',font=('consolas',15))
        r5.place(relx=0,rely=0.74)
        V=[var,var1,var2,var3,var4]
        pay=Button(WIN4,text="Proceed to pay bill",command=bill,font=("Arial",20),bg="#B7E9F7")
        pay.place(relx=0.35,rely=0.8)
        BB2=Button(WIN4,text="back",command=Z1,font=("Arial",20),bg="#B7E9F7")
        BB2.place(relx=0.72,rely=0.65)
        if(CLIST[1]!=0):
            CB2.state('DISABLED')
        CB2=Button(WIN4,text="confirm",command=B,font=("Arial",20),bg="#B7E9F7")
        CB2.place(relx=0.72,rely=0.75)
    else:
        WIN4.deiconify()
    C2=C2+1
    
def haircut():
    global CB3,C3,WIN5,A2,kk1,kk2,kk3,kk4,kk5,zz1,zz2,zz3,zz4,zz5,ss4,ss5,ss1,ss2,ss3,AAA1,AAA3,AAA2,AAA4,AAA6,AAA5,pay,V,ti,BILL,count
    ti="haircut"
    C=lambda t=3:confirm(t);Z2=lambda :back(WIN5)
    if(C3==0):
        WIN5=Toplevel()
        WIN5.state('zoomed')
        WIN5.config(bg="#ffdddd")
        A2=Label(WIN5,text='Haircut',bg='#ffdddd',fg='#0000FF',font=("Consolas",60))                 
        A2.place(relx=0.3,rely=0.050)
        kk1=ImageTk.PhotoImage(Image.open(add+r"\hair.jpg"))
        kk2=ImageTk.PhotoImage(Image.open(add+r"\hair1.jpg"))
        kk3=ImageTk.PhotoImage(Image.open(add+r"\hair2.jpg"))
        kk4=ImageTk.PhotoImage(Image.open(add+r"\hair3.jpg"))
        kk5=ImageTk.PhotoImage(Image.open(add+r"\hair4.jpg"))

        zz1=IntVar();zz2=IntVar();zz3=IntVar();zz4=IntVar();zz5=IntVar()
        ss1=Checkbutton(WIN5,image=kk1,var=zz1,onvalue=8000,bg="#ffdddd")
        ss2=Checkbutton(WIN5,image=kk2,var=zz2,onvalue=850,bg="#ffdddd")
        ss3=Checkbutton(WIN5,image=kk3,var=zz3,onvalue=400,bg="#ffdddd")
        ss4=Checkbutton(WIN5,image=kk4,var=zz4,onvalue=10000,bg="#ffdddd")
        ss5=Checkbutton(WIN5,image=kk5,var=zz5,onvalue=2000,bg="#ffdddd")
        ss1.place(relx=0.1,rely=0.2);ss2.place(relx=0.1,rely=0.32);ss3.place(relx=0.1,rely=0.44);ss4.place(relx=0.1,rely=0.56);ss5.place(relx=0.1,rely=0.68)

        AAA1=Label(WIN5,text='Hair Straightening',bg='#ffdddd',fg='black',font=("Calibri",20));
        AAA2=Label(WIN5,text='Feather and Layer',bg='#ffdddd',fg='black',font=("Calibri",20));
        AAA3=Label(WIN5,text='U cut',bg='#ffdddd',fg='black',font=("Calibri",20));
        AAA4=Label(WIN5,text='Keratin treatment',bg='#ffdddd',fg='black',font=("Calibri",20));
        AAA5=Label(WIN5,text='Hair spa',bg='#ffdddd',fg='black',font=("Calibri",20));
        AAA1.place(relx=0.25,rely=0.2);AAA2.place(relx=0.25,rely=0.32);AAA3.place(relx=0.25,rely=0.44);AAA4.place(relx=0.25,rely=0.56);AAA5.place(relx=0.25,rely=0.68)
        BBB1=Label(WIN5,text='Rs 8000',bg='#ffdddd',fg='black',font=("Calibri",20));
        BBB2=Label(WIN5,text='Rs 850',bg='#ffdddd',fg='black',font=("Calibri",20));
        BBB3=Label(WIN5,text='Rs 400',bg='#ffdddd',fg='black',font=("Calibri",20));
        BBB4=Label(WIN5,text='Rs 10000',bg='#ffdddd',fg='black',font=("Calibri",20));
        BBB5=Label(WIN5,text='Rs 2000',bg='#ffdddd',fg='black',font=("Calibri",20));
        BBB1.place(relx=0.5,rely=0.2);BBB2.place(relx=0.5,rely=0.32);BBB3.place(relx=0.5,rely=0.44);BBB4.place(relx=0.5,rely=0.56);BBB5.place(relx=0.5,rely=0.68);
        pay=Button(WIN5,text="Proceed to pay bill",command=bill,font=("Arial",20),bg="#B7E9F7")
        pay.place(relx=0.68,rely=0.5)
        V=[zz1,zz2,zz3,zz4,zz5]
        if(CLIST[2]!=0):
            CB3.state('DISABLED')
        CB3=Button(WIN5,text="confirm",command=C,font=("Arial",20),bg="#B7E9F7")
        CB3.place(relx=0.68,rely=0.75)
        BB3=Button(WIN5,text="back",command=Z2,font=("Arial",20),bg="#B7E9F7")
        BB3.place(relx=0.68,rely=0.65)
    else:
        WIN5.deiconify()
    C3=C3+1

def mehendi():
    global CB4,WIN6,AA1,kl,k1,k2,k3,k4,k5,k6,z1,z2,z3,z4,z5,z6,s4,s5,s6,AA1,AA3,AA5,s1,s2,s3,AA2,AA4,AA6,pay,V,ti,BILL,count,C4
    ti="mehendi"
    D=lambda t=4:confirm(t);Z3=lambda :back(WIN6)
    if(C4==0):
        WIN6=Toplevel()
        WIN6.state('zoomed')
        WIN6.config(bg="#ffdddd")
        AAl=Label(WIN6,text='Mehendi',bg='#ffdddd',fg='#0000FF',font=("Lucida",50))                 
        AAl.place(relx=0.3,rely=0.050)
        k1=ImageTk.PhotoImage(Image.open(add+r"\meh2.jpg"))
        k2=ImageTk.PhotoImage(Image.open(add+r"\meh3.jpg"))
        k3=ImageTk.PhotoImage(Image.open(add+r"\meh1.jpg"))
        k4=ImageTk.PhotoImage(Image.open(add+r"\Foot1.jpg"))
        k5=ImageTk.PhotoImage(Image.open(add+r"\bangle.jpg"))
        k6=ImageTk.PhotoImage(Image.open(add+r"\lace.jpg"))


        z1=IntVar();z2=IntVar();z3=IntVar(); z4=IntVar();z5=IntVar();z6=IntVar()
        s1=Checkbutton(WIN6,image=k1,var=z1,onvalue=500,bg="#ffdddd")
        s2=Checkbutton(WIN6,image=k2,var=z2,onvalue=2000,bg="#ffdddd")
        s3=Checkbutton(WIN6,image=k3,var=z3,onvalue=400,bg="#ffdddd")
        s4=Checkbutton(WIN6,image=k4,var=z4,onvalue=1000,bg="#ffdddd")
        s5=Checkbutton(WIN6,image=k5,var=z5,onvalue=600,bg="#ffdddd")
        s6=Checkbutton(WIN6,image=k6,var=z6,onvalue=550,bg="#ffdddd")


        s1.place(relx=0.1,rely=0.2);s2.place(relx=0.1,rely=0.32);s3.place(relx=0.1,rely=0.43);s4.place(relx=0.1,rely=0.55);s5.place(relx=0.1,rely=0.68);s6.place(relx=0.1,rely=0.80)
        AA2=Label(WIN6,text='Arabic',bg='#ffdddd',fg='black',font=("Calibri",20));
        AA4=Label(WIN6,text='Bridal',bg='#ffdddd',fg='black',font=("Calibri",20));
        AA6=Label(WIN6,text='Simple',bg='#ffdddd',fg='black',font=("Calibri",20));
        AA1=Label(WIN6,text='Foot Mehendi',bg='#ffdddd',fg='black',font=("Calibri",20));
        AA3=Label(WIN6,text='Bangle',bg='#ffdddd',fg='black',font=("Calibri",20));
        AA5=Label(WIN6,text='Lace',bg='#ffdddd',fg='black',font=("Calibri",20));
        AA2.place(relx=0.25,rely=0.2);AA4.place(relx=0.25,rely=0.32);AA6.place(relx=0.25,rely=0.43);AA1.place(relx=0.25,rely=0.55);AA3.place(relx=0.25,rely=0.68);AA5.place(relx=0.25,rely=0.80)
        BB1=Label(WIN6,text='Rs 500',bg='#ffdddd',fg='black',font=("Calibri",20));
        BB3=Label(WIN6,text='Rs 2000',bg='#ffdddd',fg='black',font=("Calibri",20));
        BB5=Label(WIN6,text='Rs 400',bg='#ffdddd',fg='black',font=("Calibri",20));
        BB2=Label(WIN6,text='Rs 1000',bg='#ffdddd',fg='black',font=("Calibri",20));
        BB4=Label(WIN6,text='Rs 600',bg='#ffdddd',fg='black',font=("Calibri",20));
        BB6=Label(WIN6,text='Rs 550',bg='#ffdddd',fg='black',font=("Calibri",20));
        BB1.place(relx=0.5,rely=0.2);BB3.place(relx=0.5,rely=0.32);BB5.place(relx=0.5,rely=0.43);BB2.place(relx=0.5,rely=0.55);BB4.place(relx=0.5,rely=0.68);BB6.place(relx=0.5,rely=0.80)
        pay=Button(WIN6,text="Proceed to pay bill",command=bill,font=("Arial",20),bg="#B7E9F7")
        pay.place(relx=0.68,rely=0.5)
        V=[z1,z2,z3,z4,z5,z6]
        if(CLIST[3]!=0):
            CB4.state('DISABLED')
        CB4=Button(WIN6,text="confirm",command=D,font=("Arial",20),bg="#B7E9F7")
        CB4.place(relx=0.68,rely=0.75)
        BB4=Button(WIN6,text="back",command=Z3,font=("Arial",20),bg="#B7E9F7")
        BB4.place(relx=0.68,rely=0.65)
    else:
        WIN6.deiconify()
    C4=C4+1
def beautyspa():
    global CB5,WIN7,A1,i1,i2,i3,i4,i5,i6,v1,v2,v3,v4,v5,v6,c1,c2,c3,c4,c5,c6,A2,A3,A4,A5,A6,A7,pay,V,ti,BILL,count,C6
    ti="beautyspa"
    if(C6==0):
        E=lambda t=5:confirm(t);Z4=lambda :back(WIN7)
        WIN7=Toplevel()
        WIN7.state('zoomed')
        WIN7.config(bg="#ffdddd")
        Al=Label(WIN7,text='Beauty and Spa',bg='#ffdddd',fg='#0000FF',font=("Consolas",60))                 
        Al.place(relx=0.3,rely=0.050)
        i1=ImageTk.PhotoImage(Image.open(add+r"\headspa.jpg"))
        i2=ImageTk.PhotoImage(Image.open(add+r"\footspa.jpg"))
        i3=ImageTk.PhotoImage(Image.open(add+r"\threading.jpg"))
        i4=ImageTk.PhotoImage(Image.open(add+r"\makeup.jpg"))
        i5=ImageTk.PhotoImage(Image.open(add+r"\facial.jpg"))
        i6=ImageTk.PhotoImage(Image.open(add+r"\pedicure.jpg"))
        v1=IntVar();v2=IntVar();v3=IntVar();v4=IntVar();v5=IntVar();v6=IntVar()
        c1=Checkbutton(WIN7,image=i1,var=v1,onvalue=299,bg="#ffdddd")
        c2=Checkbutton(WIN7,image=i2,var=v2,onvalue=300,bg="#ffdddd")
        c3=Checkbutton(WIN7,image=i3,var=v3,onvalue=50,bg="#ffdddd")
        c4=Checkbutton(WIN7,image=i4,var=v4,onvalue=999,bg="#ffdddd")
        c5=Checkbutton(WIN7,image=i5,var=v5,onvalue=299,bg="#ffdddd")
        c6=Checkbutton(WIN7,image=i6,var=v6,onvalue=500,bg="#ffdddd")
        c1.place(relx=0.1,rely=0.2);c2.place(relx=0.1,rely=0.32);c3.place(relx=0.1,rely=0.44);c4.place(relx=0.1,rely=0.56);c5.place(relx=0.1,rely=0.68);c6.place(relx=0.1,rely=0.8)
        A2=Label(WIN7,text='Headspa',bg='#ffdddd',fg='black',font=("Calibri",20));A3=Label(WIN7,text='Footspa',bg='#ffdddd',fg='black',font=("Calibri",20))
        A4=Label(WIN7,text='Threading',bg='#ffdddd',fg='black',font=("Calibri",20));A5=Label(WIN7,text='Makeup',bg='#ffdddd',fg='black',font=("Calibri",20))
        A6=Label(WIN7,text='Facial',bg='#ffdddd',fg='black',font=("Calibri",20));A7=Label(WIN7,text='Pedicure&Manicure',bg='#ffdddd',fg='black',font=("Calibri",20))
        A2.place(relx=0.25,rely=0.2);A3.place(relx=0.25,rely=0.32);A4.place(relx=0.25,rely=0.44);A5.place(relx=0.25,rely=0.56);A6.place(relx=0.25,rely=0.68);A7.place(relx=0.25,rely=0.8)
        B1=Label(WIN7,text='Rs 299',bg='#ffdddd',fg='black',font=("Calibri",20));B2=Label(WIN7,text='Rs 300',bg='#ffdddd',fg='black',font=("Calibri",20))
        B3=Label(WIN7,text='Rs 50',bg='#ffdddd',fg='black',font=("Calibri",20));B4=Label(WIN7,text='Rs 999',bg='#ffdddd',fg='black',font=("Calibri",20))
        B5=Label(WIN7,text='Rs 299',bg='#ffdddd',fg='black',font=("Calibri",20));B6=Label(WIN7,text='Rs 500',bg='#ffdddd',fg='black',font=("Calibri",20))
        B1.place(relx=0.5,rely=0.2);B2.place(relx=0.5,rely=0.32);B3.place(relx=0.5,rely=0.44);B4.place(relx=0.5,rely=0.56);B5.place(relx=0.5,rely=0.68);B6.place(relx=0.5,rely=0.8)
        pay=Button(WIN7,text="Proceed to pay bill",command=bill,font=("Arial",20),bg="#B7E9F7")
        pay.place(relx=0.68,rely=0.5)
        V=[v1,v2,v3,v4,v5,v6]
        if(CLIST[4]!=0):
            CB5.state('DISABLED')
        CB5=Button(WIN7,text="confirm",command=E,font=("Arial",20),bg="#B7E9F7")
        CB5.place(relx=0.68,rely=0.75)
        BB5=Button(WIN7,text="back",command=Z4,font=("Arial",20),bg="#B7E9F7")
        BB5.place(relx=0.68,rely=0.65) 
    else:
        WIN7.deiconify()
        
    C6=C6+1

def hm():
    global ll1,bb1,win2,ll2,ll3,ll4,bb2,bb3,bb4,ll5,bb5
    ll1=ImageTk.PhotoImage(Image.open(add+r"\g6.jpg"))
    ll2=ImageTk.PhotoImage(Image.open(add+r"\g9.jpg"))
    ll3=ImageTk.PhotoImage(Image.open(add+r"\g7.jpg"))
    ll4=ImageTk.PhotoImage(Image.open(add+r"\bride1.jpeg"))
    ll5=ImageTk.PhotoImage(Image.open(add+r"\g5.jpg")) 
    bb1=Button(win2,image=ll1,command=nailart)
    bb2=Button(win2,image=ll2,command=mehendi)
    bb3=Button(win2,image=ll3,command=haircut)
    bb4=Button(win2,image=ll4,command=bridal)
    bb5=Button(win2,image=ll5,command=beautyspa)
    bb1.place(relx=0,rely=0.6)
    bb2.place(relx=0.2,rely=0.6)
    bb3.place(relx=0.4,rely=0.6)
    bb4.place(relx=0.6,rely=0.6)
    bb5.place(relx=0.8,rely=0.6)
def ss():
    global kk,c,l4,l5,l6,l7,l8,win2
    if(c==5):
        c=0
        kk[4].place_forget()
        kk[0].place(relx=0.30,rely=0)
    else:
        kk[c-1].place_forget()
        kk[c].place(relx=0.30,rely=0)
    c=c+1
    win2.after(2000,ss)
def ssi():
    global l4,l5,l6,l7,l8,t1,t2,t3,t4,t5,win2,c,kk
    l4=ImageTk.PhotoImage(Image.open(add+r"\briidaloff.jpg"))
    l5=ImageTk.PhotoImage(Image.open(add+r"\offer.png"))
    l6=ImageTk.PhotoImage(Image.open(add+r"\facialr.jpg"))
    l7=ImageTk.PhotoImage(Image.open(add+r"\nailartoff.jpg"))
    l8=ImageTk.PhotoImage(Image.open(add+r"\haircutoff.jpg")) 
    t1=Label(win2,image=l8)
    t2=Label(win2,image=l5)
    t3=Label(win2,image=l6)
    t4=Label(win2,image=l4)
    t5=Label(win2,image=l7)
    kk=[t1,t2,t3,t4,t5]
    c=1
    t1.place(relx=0.30,rely=0)
    win2.after(2000,ss)
def usc():
    global win2,C,cur
    F=open(r"C:\Users\Lahari\Desktop\forsql.txt","r")
    P=F.read().split('\n')
    C=mysql.connector.connect(user='root',password=P[0],host='127.0.0.1',database='userdetails')
    cur=C.cursor()
    cur.execute("select * from details")
    LIS=cur.fetchall();COUNT=0
    for i in LIS:
        if(i[1]==e1.get() and i[2]==e2.get()):
          break
        COUNT=COUNT+1
    
    

   
    if(COUNT==len(LIS)):
        l3=Label(text='invalid password or user name')
        l3.place(relx=0.43,rely=0.85)
        
    else:
        win2=Toplevel()
        win2.config(bg='#FFC8FB')
        win2.state('zoomed')
        win2.after(1,hm) 
        win2.after(1,ssi)
def lsc():
    global win2,nl
    if(len(e3.get())==0 or len(e4.get())==0 or len(e5.get())==0 or (e5.get()).isnumeric()==False):
        nl=Label(win1,text="Please enter the details properly")
        nl.place(relx=0.43,rely=0.85)
    else:
        F=open(r"C:\Users\Lahari\Desktop\forsql.txt","r")
        P=F.read().split('\n')
        C=mysql.connector.connect(user='root',password=P[0],host='127.0.0.1',database='userdetails')
        cur=C.cursor()
        cur.execute("select * from details")
        userno=len(cur.fetchall())+1
        print(userno)
        cur.execute("insert into details values(%s,%s,%s);",(userno,e3.get(),e4.get()))
        C.commit()
        win2=Toplevel()
        win2.config(bg='#FFC8FB')
        win2.state('zoomed')
        win2.after(10,hm)
        win2.after(500,ssi)
def sign_in():
    global e3,e4,e5
    name=Label(text='NAME',font=('Courier',10),bg='#B7E9F7')
    name.place(relx=0.38,rely=0.68)
    pw=Label(text='PASSWORD',font=('Courier',10),bg='#B7E9F7')
    pw.place(relx=0.38,rely=0.73)
    e3=Entry()
    e3.place(relx=0.58,rely=0.68)
    e4=Entry(show='*')
    e4.place(relx=0.58,rely=0.73)
    pno=Label(text='PHONE NUMBER',font=('Courier',10),bg='#B7E9F7')
    pno.place(relx=0.38,rely=0.78)
    e5=Entry()
    e5.place(relx=0.58,rely=0.78)
    
    b4=Button(text='enter',command=lsc,bg='#B7E9F7')
    b4.place(relx=0.58,rely=0.83)
def log_in():
    global e1,e2,b3,l2
    name=Label(text='NAME',font=('Courier',10),bg='#B7E9F7')
    name.place(relx=0.38,rely=0.68)
    pw=Label(text='PASSWORD',font=('Courier',10),bg='#B7E9F7')
    pw.place(relx=0.38,rely=0.73)
    e1=Entry()
    e1.place(relx=0.58,rely=0.68)
    e2=Entry(show='*')
    e2.place(relx=0.58,rely=0.73)
    b3=Button(text='enter',command=usc,bg='#B7E9F7')
    b3.place(relx=0.58,rely=0.83)
def f1():
    global l1,win1,b1,b2,p2
    l1.destroy()
    p2=ImageTk.PhotoImage(Image.open(add+r'\welcomepage.png'))
    l2=Label(image=p2)
    l2.grid()
    b1=Button(text='sign up',height=2,width=15,bg='#B7E9F7',command=sign_in)
    b2=Button(text='log in',height=2,width=15,command=log_in,bg='#B7E9F7')
    b1.place(relx=0.38,rely=0.60)
    b2.place(relx=0.58,rely=0.60)
win1=Tk()
win1.state('zoomed')
p1=ImageTk.PhotoImage(Image.open(add+r"\sample1.png"))
l1=Label(image=p1)
l1.grid()
win1.after(8000,f1)
win1.config(bg='#ffdddd')
win1.mainloop()
