from tkinter import *
from PIL import ImageTk,Image
count=0;ti='hi';temmp=0;V=[];sums=0;BILL=[];fcount=0
def confirm():
    global win3,BILL,V
    for i in V:
        if(i.get()!=0):
            BILL.append(i.get())
    
def bdetails():
    global f2,fd,ti,fcount
    
    if(len(BE1.get())==0 or len(BE2.get())==0 or len(BE3.get("1.0","end-1c"))==0 or len(BE4.get())==0 or len(BE5.get())==0 or (BE5.get()).isnumeric()==False):
        nl=Label(win4,text="Please enter the details properly",bg="#ffdddd",fg="black")
        nl.place(relx=0.45,rely=0.55)
    else:
        
        f2=open("new.py","a+")
        f2.write(BE4.get()+','+BE5.get()+','+BE1.get()+','+BE2.get()+','+BE3.get("1.0","end-1c")+','+sums+','+ti+","+'\n')
        f2.close()
        F=open("count.py","r+")
        fcount=int(F.read())
        F.seek(0)
        fd=open("bdetails.py","r")
        listd=fd.readlines();length=len(listd)
        f=list(listd[fcount].split(','))
        fcount=fcount+1
        F.write(str(fcount))
        dl1=Label(win4,text="Your beautician details\nName:"+f[0]+'\n'+"Phonenumber:"+f[1],font=("Consolas",15),bg="#ffdddd",fg="#0000FF")
        dl1.place(relx=0.42,rely=0.7)
        
def back():
    global win3,count
    count=count+1
    win3.withdraw()
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
    Tl=Label(win4,text='Thank you for using Hormoso',bg='#ffdddd',fg='#0000FF',font=("Consolas",60))                 
    Tl.place(relx=0.1,rely=0.050)
    Bill=Label(win4,text="Your total bill is "+sums,bg='#ffdddd',fg='#0000FF',font=("Consolas",20))                 
    Bill.place(relx=0.37,rely=0.18)
    BE4=Entry(win4);BE5=Entry(win4)
    BE1=Entry(win4);BE2=Entry(win4);BE3=Text(win4,height=5,width=30);L1=Label(win4,text='Date:',bg='#ffdddd',font=("Arial",12));L2=Label(win4,text='Timings:',bg='#ffdddd',font=("Arial",12))
    L3=Label(win4,text='Address:',bg='#ffdddd',font=("Arial",12));L4=Label(win4,text='Name:',bg='#ffdddd',font=("Arial",12));L5=Label(win4,text='Phone no:',bg='#ffdddd',font=("Arial",12))
    L1.place(relx=0.4,rely=0.35);L2.place(relx=0.4,rely=0.4);L3.place(relx=0.4,rely=0.45),L5.place(relx=0.4,rely=0.3);L4.place(relx=0.4,rely=0.25)
    BE1.place(relx=0.55,rely=0.35);BE2.place(relx=0.55,rely=0.4);BE3.place(relx=0.55,rely=0.45);BE5.place(relx=0.55,rely=0.3);BE4.place(relx=0.55,rely=0.25)
    Bu=Button(win4,text='Enter',bg='#B7E9F7',font=("Arial",12),command=bdetails)
    Bu.place(relx=0.475,rely=0.6)
    count=count+1
def nailart():
    global x1,x2,x3,x4,x5,e1,e2,e3,e4,e5,b1,b2,b3,b4,b5,D2,D3,D4,D5,D6,pay,V,D1,F1,F2,F3,F4,F5,ti,BILL,win3,count
    ti="nailart"
    win3=Toplevel()
    win3.state('zoomed')
    win3.config(bg="#ffdddd")
    Dl=Label(win3,text='Nail Art',bg='#ffdddd',fg='#0000FF',font=("Consolas",60))                 
    Dl.place(relx=0.3,rely=0.050)
    x1=ImageTk.PhotoImage(Image.open("Stensil.jpg"))
    x2=ImageTk.PhotoImage(Image.open("Air brush.jpg"))
    x3=ImageTk.PhotoImage(Image.open("foot.jpg"))
    x4=ImageTk.PhotoImage(Image.open("simple.jpg"))
    x5=ImageTk.PhotoImage(Image.open("stylish.jpg"))
    e1=IntVar();e2=IntVar();e3=IntVar();e4=IntVar();e5=IntVar()
    b1=Checkbutton(win3,image=x1,var=e1,onvalue=175,bg="#ffdddd")
    b2=Checkbutton(win3,image=x2,var=e2,onvalue=250,bg="#ffdddd")
    b3=Checkbutton(win3,image=x3,var=e3,onvalue=150,bg="#ffdddd")
    b4=Checkbutton(win3,image=x4,var=e4,onvalue=200,bg="#ffdddd")
    b5=Checkbutton(win3,image=x5,var=e5,onvalue=300,bg="#ffdddd")
    b1.place(relx=0.1,rely=0.2);b2.place(relx=0.1,rely=0.32);b3.place(relx=0.1,rely=0.44);b4.place(relx=0.1,rely=0.56);b5.place(relx=0.1,rely=0.68)
    D2=Label(win3,text='Stensil',bg='#ffdddd',fg='black',font=("Calibri",20));D3=Label(win3,text='Air brush',bg='#ffdddd',fg='black',font=("Calibri",20))
    D4=Label(win3,text='Foot',bg='#ffdddd',fg='black',font=("Calibri",20));D5=Label(win3,text='Simple',bg='#ffdddd',fg='black',font=("Calibri",20))
    D6=Label(win3,text='Stylish',bg='#ffdddd',fg='black',font=("Calibri",20))
    D2.place(relx=0.25,rely=0.2);D3.place(relx=0.25,rely=0.32);D4.place(relx=0.25,rely=0.44);D5.place(relx=0.25,rely=0.56);D6.place(relx=0.25,rely=0.68)
    F1=Label(win3,text='Rs 175',bg='#ffdddd',fg='black',font=("Calibri",20));F2=Label(win3,text='Rs 250',bg='#ffdddd',fg='black',font=("Calibri",20))
    F3=Label(win3,text='Rs 150',bg='#ffdddd',fg='black',font=("Calibri",20));F4=Label(win3,text='Rs 200',bg='#ffdddd',fg='black',font=("Calibri",20))
    F5=Label(win3,text='Rs 300',bg='#ffdddd',fg='black',font=("Calibri",20))
    F1.place(relx=0.5,rely=0.2);F2.place(relx=0.5,rely=0.32);F3.place(relx=0.5,rely=0.44);F4.place(relx=0.5,rely=0.56);F5.place(relx=0.5,rely=0.68)
    pay=Button(win3,text="Proceed to pay bill",command=bill,font=("Arial",20),bg="#B7E9F7")
    pay.place(relx=0.68,rely=0.5)
    V=[e1,e2,e3,e4,e5]
    BB1=Button(win3,text="back",command=back,font=("Arial",20),bg="#B7E9F7")
    BB1.place(relx=0.68,rely=0.65)
    CB1=Button(win3,text="confirm",command=confirm,font=("Arial",20),bg="#B7E9F7")
    CB1.place(relx=0.68,rely=0.75)
def bridal():
    global i1,tt,i2,tt1,i3,tt2,i4,tt3,i5,tt4,i6,tt5,var,var1,var2,var3,var4,V,ti,BILL,win3,count
    ti="bridal"
    i2=ImageTk.PhotoImage(Image.open("bridal4.jpg"))
    i3=ImageTk.PhotoImage(Image.open("UrbanClap.jpg"))
    i4=ImageTk.PhotoImage(Image.open("bridal2.jpg"))
    i5=ImageTk.PhotoImage(Image.open("bridal.jpg"))
    i6=ImageTk.PhotoImage(Image.open("bridal3.jpg"))
    var=IntVar()
    var1=IntVar()
    var2=IntVar()
    var3=IntVar()
    var4=IntVar()
    win3=Toplevel()
    win3.state('zoomed')
    win3.config(bg='#ffdddd')
    h1=Label(win3,text='Bridal Packages',bg='#ffdddd',font=('consolas',25))
    h1.place(relx=0.35,rely=0)
    r1=Checkbutton(win3,text=' Traditional Bridal Makeup \n price:20,000 for one time draping,makeup and hairstyling',variable=var,onvalue=20000,offvalue=0,bg='#ffdddd',fg='#0000FF',font=('consolas',15))
    tt1=Label(win3,image=i2)
    tt2=Label(win3,image=i3)
    tt3=Label(win3,image=i4)
    tt4=Label(win3,image=i5)
    tt5=Label(win3,image=i6)
    tt1.place(relx=0.59,rely=0.1)
    tt2.place(relx=0.62,rely=0.25)
    tt3.place(relx=0.62,rely=0.4)
    tt4.place(relx=0.62,rely=0.57)
    tt5.place(relx=0.62,rely=0.74)
    r1.place(relx=0,rely=0.1)
    r2=Checkbutton(win3,text='Reception Bridal Package \n price:18,000 for draping sarees in different styles,hairstyling,makeup',variable=var1,onvalue=18000,offvalue=0,bg='#ffdddd',fg='#0000FF',font=('consolas',15))
    r2.place(relx=0,rely=0.25)
    r3=Checkbutton(win3,text='Airbrush Bridal Makeup \n price:22,000 for draping sarees in different styles,hairstyling \n airbrush makeup(flawless finish,light-weight makeup)',variable=var2,onvalue=22000,offvalue=0,bg='#ffdddd',fg='#0000FF',font=('consolas',15))
    r3.place(relx=0,rely=0.4)
    r4=Checkbutton(win3,text='Mineral Bridal Makeup \n price:23,000 for draping sarees in different styles,hairstyling \n mineral makeup(natural,flawless finish,chemical-free composition)',variable=var3,onvalue=23000,offvalue=0,bg='#ffdddd',fg='#0000FF',font=('consolas',15))
    r4.place(relx=0,rely=0.57)
    r5=Checkbutton(win3,text='Muslim Bridal Makeup \n price:19,000 for  one time draping ,hairstyling , makeup',variable=var4,onvalue=19000,offvalue=0,bg='#ffdddd',fg='#0000FF',font=('consolas',15))
    r5.place(relx=0,rely=0.74)
    V=[var,var1,var2,var3,var4]
    pay=Button(win3,text="Proceed to pay bill",command=bill,font=("Arial",20),bg="#B7E9F7")
    pay.place(relx=0.35,rely=0.8)
    BB2=Button(win3,text="back",command=back,font=("Arial",20),bg="#B7E9F7")
    BB2.place(relx=0.72,rely=0.65)
    CB2=Button(win3,text="confirm",command=confirm,font=("Arial",20),bg="#B7E9F7")
    CB2.place(relx=0.72,rely=0.75)
    
def haircut():
    global win3,A2,kk1,kk2,kk3,kk4,kk5,zz1,zz2,zz3,zz4,zz5,ss4,ss5,ss1,ss2,ss3,AAA1,AAA3,AAA2,AAA4,AAA6,AAA5,pay,V,ti,BILL,count
    ti="haircut"
    win3=Toplevel()
    win3.state('zoomed')
    win3.config(bg="#ffdddd")
    A2=Label(win3,text='Haircut',bg='#ffdddd',fg='#0000FF',font=("Consolas",60))                 
    A2.place(relx=0.3,rely=0.050)
    kk1=ImageTk.PhotoImage(Image.open("hair.jpg"))
    kk2=ImageTk.PhotoImage(Image.open("hair1.jpg"))
    kk3=ImageTk.PhotoImage(Image.open("hair2.jpg"))
    kk4=ImageTk.PhotoImage(Image.open("hair3.jpg"))
    kk5=ImageTk.PhotoImage(Image.open("hair4.jpg"))
    
    zz1=IntVar();zz2=IntVar();zz3=IntVar();zz4=IntVar();zz5=IntVar()
    ss1=Checkbutton(win3,image=kk1,var=zz1,onvalue=8000,bg="#ffdddd")
    ss2=Checkbutton(win3,image=kk2,var=zz2,onvalue=850,bg="#ffdddd")
    ss3=Checkbutton(win3,image=kk3,var=zz3,onvalue=400,bg="#ffdddd")
    ss4=Checkbutton(win3,image=kk4,var=zz4,onvalue=10000,bg="#ffdddd")
    ss5=Checkbutton(win3,image=kk5,var=zz3,onvalue=2000,bg="#ffdddd")
    ss1.place(relx=0.1,rely=0.2);ss2.place(relx=0.1,rely=0.32);ss3.place(relx=0.1,rely=0.44);ss4.place(relx=0.1,rely=0.56);ss5.place(relx=0.1,rely=0.68)
    
    AAA1=Label(win3,text='Hair Straightening',bg='#ffdddd',fg='black',font=("Calibri",20));
    AAA2=Label(win3,text='Feather and Layer',bg='#ffdddd',fg='black',font=("Calibri",20));
    AAA3=Label(win3,text='U cut',bg='#ffdddd',fg='black',font=("Calibri",20));
    AAA4=Label(win3,text='Keratin treatment',bg='#ffdddd',fg='black',font=("Calibri",20));
    AAA5=Label(win3,text='Hair spa',bg='#ffdddd',fg='black',font=("Calibri",20));
    AAA1.place(relx=0.25,rely=0.2);AAA2.place(relx=0.25,rely=0.32);AAA3.place(relx=0.25,rely=0.44);AAA4.place(relx=0.25,rely=0.56);AAA5.place(relx=0.25,rely=0.68)
    BBB1=Label(win3,text='Rs 8000',bg='#ffdddd',fg='black',font=("Calibri",20));
    BBB2=Label(win3,text='Rs 850',bg='#ffdddd',fg='black',font=("Calibri",20));
    BBB3=Label(win3,text='Rs 400',bg='#ffdddd',fg='black',font=("Calibri",20));
    BBB4=Label(win3,text='Rs 10000',bg='#ffdddd',fg='black',font=("Calibri",20));
    BBB5=Label(win3,text='Rs 2000',bg='#ffdddd',fg='black',font=("Calibri",20));
    BBB1.place(relx=0.5,rely=0.2);BBB2.place(relx=0.5,rely=0.32);BBB3.place(relx=0.5,rely=0.44);BBB4.place(relx=0.5,rely=0.56);BBB5.place(relx=0.5,rely=0.68);
    pay=Button(win3,text="Proceed to pay bill",command=bill,font=("Arial",20),bg="#B7E9F7")
    pay.place(relx=0.68,rely=0.5)
    V=[zz1,zz2,zz3,zz4,zz5]
    CB3=Button(win3,text="confirm",command=confirm,font=("Arial",20),bg="#B7E9F7")
    CB3.place(relx=0.68,rely=0.75)
    BB3=Button(win3,text="back",command=back,font=("Arial",20),bg="#B7E9F7")
    BB3.place(relx=0.68,rely=0.65)

def mehendi():
    global win3,AA1,kl,k1,k2,k3,k4,k5,k6,z1,z2,z3,z4,z5,z6,s4,s5,s6,AA1,AA3,AA5,s1,s2,s3,AA2,AA4,AA6,pay,V,ti,BILL,count
    ti="mehendi"
    win3=Toplevel()
    win3.state('zoomed')
    win3.config(bg="#ffdddd")
    AAl=Label(win3,text='Mehendi',bg='#ffdddd',fg='#0000FF',font=("Lucida",50))                 
    AAl.place(relx=0.3,rely=0.050)
    k1=ImageTk.PhotoImage(Image.open("meh2.jpg"))
    k2=ImageTk.PhotoImage(Image.open("meh3.jpg"))
    k3=ImageTk.PhotoImage(Image.open("meh1.jpg"))
    k4=ImageTk.PhotoImage(Image.open("Foot1.jpg"))
    k5=ImageTk.PhotoImage(Image.open("bangle.jpg"))
    k6=ImageTk.PhotoImage(Image.open("lace.jpg"))
    
    
    z1=IntVar();z2=IntVar();z3=IntVar(); z4=IntVar();z5=IntVar();z6=IntVar()
    s1=Checkbutton(win3,image=k1,var=z1,onvalue=500,bg="#ffdddd")
    s2=Checkbutton(win3,image=k2,var=z2,onvalue=2000,bg="#ffdddd")
    s3=Checkbutton(win3,image=k3,var=z3,onvalue=400,bg="#ffdddd")
    s4=Checkbutton(win3,image=k4,var=z4,onvalue=1000,bg="#ffdddd")
    s5=Checkbutton(win3,image=k5,var=z5,onvalue=600,bg="#ffdddd")
    s6=Checkbutton(win3,image=k6,var=z6,onvalue=550,bg="#ffdddd")
    
    
    s1.place(relx=0.1,rely=0.2);s2.place(relx=0.1,rely=0.32);s3.place(relx=0.1,rely=0.43);s4.place(relx=0.1,rely=0.55);s5.place(relx=0.1,rely=0.68);s6.place(relx=0.1,rely=0.80)
    AA2=Label(win3,text='Arabic',bg='#ffdddd',fg='black',font=("Calibri",20));
    AA4=Label(win3,text='Bridal',bg='#ffdddd',fg='black',font=("Calibri",20));
    AA6=Label(win3,text='Simple',bg='#ffdddd',fg='black',font=("Calibri",20));
    AA1=Label(win3,text='Foot Mehendi',bg='#ffdddd',fg='black',font=("Calibri",20));
    AA3=Label(win3,text='Bangle',bg='#ffdddd',fg='black',font=("Calibri",20));
    AA5=Label(win3,text='Lace',bg='#ffdddd',fg='black',font=("Calibri",20));
    AA2.place(relx=0.25,rely=0.2);AA4.place(relx=0.25,rely=0.32);AA6.place(relx=0.25,rely=0.43);AA1.place(relx=0.25,rely=0.55);AA3.place(relx=0.25,rely=0.68);AA5.place(relx=0.25,rely=0.80)
    BB1=Label(win3,text='Rs 500',bg='#ffdddd',fg='black',font=("Calibri",20));
    BB3=Label(win3,text='Rs 2000',bg='#ffdddd',fg='black',font=("Calibri",20));
    BB5=Label(win3,text='Rs 400',bg='#ffdddd',fg='black',font=("Calibri",20));
    BB2=Label(win3,text='Rs 1000',bg='#ffdddd',fg='black',font=("Calibri",20));
    BB4=Label(win3,text='Rs 600',bg='#ffdddd',fg='black',font=("Calibri",20));
    BB6=Label(win3,text='Rs 550',bg='#ffdddd',fg='black',font=("Calibri",20));
    BB1.place(relx=0.5,rely=0.2);BB3.place(relx=0.5,rely=0.32);BB5.place(relx=0.5,rely=0.43);BB2.place(relx=0.5,rely=0.55);BB4.place(relx=0.5,rely=0.68);BB6.place(relx=0.5,rely=0.80)
    pay=Button(win3,text="Proceed to pay bill",command=bill,font=("Arial",20),bg="#B7E9F7")
    pay.place(relx=0.68,rely=0.5)
    V=[z1,z2,z3,z4,z5,z6]
    CB4=Button(win3,text="confirm",command=confirm,font=("Arial",20),bg="#B7E9F7")
    CB4.place(relx=0.68,rely=0.75)
    BB4=Button(win3,text="back",command=back,font=("Arial",20),bg="#B7E9F7")
    BB4.place(relx=0.68,rely=0.65)
def beautyspa():
    global win3,A1,i1,i2,i3,i4,i5,i6,v1,v2,v3,v4,v5,v6,c1,c2,c3,c4,c5,c6,A2,A3,A4,A5,A6,A7,pay,V,ti,BILL,count
    ti="beautyspa"
    win3=Toplevel()
    win3.state('zoomed')
    win3.config(bg="#ffdddd")
    Al=Label(win3,text='Beauty and Spa',bg='#ffdddd',fg='#0000FF',font=("Consolas",60))                 
    Al.place(relx=0.3,rely=0.050)
    i1=ImageTk.PhotoImage(Image.open("headspa.jpg"))
    i2=ImageTk.PhotoImage(Image.open("footspa.jpg"))
    i3=ImageTk.PhotoImage(Image.open("threading.jpg"))
    i4=ImageTk.PhotoImage(Image.open("makeup.jpg"))
    i5=ImageTk.PhotoImage(Image.open("facial.jpg"))
    i6=ImageTk.PhotoImage(Image.open("pedicure.jpg"))
    v1=IntVar();v2=IntVar();v3=IntVar();v4=IntVar();v5=IntVar();v6=IntVar()
    c1=Checkbutton(win3,image=i1,var=v1,onvalue=299,bg="#ffdddd")
    c2=Checkbutton(win3,image=i2,var=v2,onvalue=300,bg="#ffdddd")
    c3=Checkbutton(win3,image=i3,var=v3,onvalue=50,bg="#ffdddd")
    c4=Checkbutton(win3,image=i4,var=v4,onvalue=999,bg="#ffdddd")
    c5=Checkbutton(win3,image=i5,var=v5,onvalue=299,bg="#ffdddd")
    c6=Checkbutton(win3,image=i6,var=v6,onvalue=500,bg="#ffdddd")
    c1.place(relx=0.1,rely=0.2);c2.place(relx=0.1,rely=0.32);c3.place(relx=0.1,rely=0.44);c4.place(relx=0.1,rely=0.56);c5.place(relx=0.1,rely=0.68);c6.place(relx=0.1,rely=0.8)
    A2=Label(win3,text='Headspa',bg='#ffdddd',fg='black',font=("Calibri",20));A3=Label(win3,text='Footspa',bg='#ffdddd',fg='black',font=("Calibri",20))
    A4=Label(win3,text='Threading',bg='#ffdddd',fg='black',font=("Calibri",20));A5=Label(win3,text='Makeup',bg='#ffdddd',fg='black',font=("Calibri",20))
    A6=Label(win3,text='Facial',bg='#ffdddd',fg='black',font=("Calibri",20));A7=Label(win3,text='Pedicure&Manicure',bg='#ffdddd',fg='black',font=("Calibri",20))
    A2.place(relx=0.25,rely=0.2);A3.place(relx=0.25,rely=0.32);A4.place(relx=0.25,rely=0.44);A5.place(relx=0.25,rely=0.56);A6.place(relx=0.25,rely=0.68);A7.place(relx=0.25,rely=0.8)
    B1=Label(win3,text='Rs 299',bg='#ffdddd',fg='black',font=("Calibri",20));B2=Label(win3,text='Rs 300',bg='#ffdddd',fg='black',font=("Calibri",20))
    B3=Label(win3,text='Rs 50',bg='#ffdddd',fg='black',font=("Calibri",20));B4=Label(win3,text='Rs 999',bg='#ffdddd',fg='black',font=("Calibri",20))
    B5=Label(win3,text='Rs 299',bg='#ffdddd',fg='black',font=("Calibri",20));B6=Label(win3,text='Rs 500',bg='#ffdddd',fg='black',font=("Calibri",20))
    B1.place(relx=0.5,rely=0.2);B2.place(relx=0.5,rely=0.32);B3.place(relx=0.5,rely=0.44);B4.place(relx=0.5,rely=0.56);B5.place(relx=0.5,rely=0.68);B6.place(relx=0.5,rely=0.8)
    pay=Button(win3,text="Proceed to pay bill",command=bill,font=("Arial",20),bg="#B7E9F7")
    pay.place(relx=0.68,rely=0.5)
    V=[v1,v2,v3,v4,v5,v6]
    CB5=Button(win3,text="confirm",command=confirm,font=("Arial",20),bg="#B7E9F7")
    CB5.place(relx=0.68,rely=0.75)
    BB5=Button(win3,text="back",command=back,font=("Arial",20),bg="#B7E9F7")
    BB5.place(relx=0.68,rely=0.65)          

def hm():
    global ll1,bb1,win2,ll2,ll3,ll4,bb2,bb3,bb4,ll5,bb5
    ll1=ImageTk.PhotoImage(Image.open("g6.jpg"))
    ll2=ImageTk.PhotoImage(Image.open("g9.jpg"))
    ll3=ImageTk.PhotoImage(Image.open("g7.jpg"))
    ll4=ImageTk.PhotoImage(Image.open("bride1.jpeg"))
    ll5=ImageTk.PhotoImage(Image.open("g5.jpg")) 
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
    l4=ImageTk.PhotoImage(Image.open("briidaloff.jpg"))
    l5=ImageTk.PhotoImage(Image.open("offer.png"))
    l6=ImageTk.PhotoImage(Image.open("facialr.jpg"))
    l7=ImageTk.PhotoImage(Image.open("nailartoff.jpg"))
    l8=ImageTk.PhotoImage(Image.open("haircutoff.jpg")) 
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
    global win2
    f=open('details.py','r')
    i=len(f.readlines())
    f.seek(0)
    for t in range(0,i+1):
        k=list(f.readline().split(','))
        if(k[0]==e1.get() and k[1]==e2.get()):
            break
    f.close()
    if(t==i):
        l3=Label(text='invalid password or user name')
        l3.place(relx=0.43,rely=0.85)
        
    else:
        win2=Toplevel()
        win2.config(bg='#ffdddd')
        win2.state('zoomed')
        win2.after(1,hm) 
        win2.after(1,ssi)
def lsc():
    global win2,nl
    if(len(e3.get())==0 or len(e4.get())==0 or len(e5.get())==0 or (e5.get()).isnumeric()==False):
        nl=Label(win1,text="Please enter the details properly")
        nl.place(relx=0.43,rely=0.85)
    else:
        f=open('details.py','a')
        f.write(e3.get()+','+e4.get()+','+e5.get()+'\n')
        win2=Toplevel()
        win2.config(bg='#ffdddd')
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
    p2=ImageTk.PhotoImage(Image.open('welcomepage.png'))
    l2=Label(image=p2)
    l2.grid()
    b1=Button(text='sign up',height=2,width=15,bg='#B7E9F7',command=sign_in)
    b2=Button(text='log in',height=2,width=15,command=log_in,bg='#B7E9F7')
    b1.place(relx=0.38,rely=0.60)
    b2.place(relx=0.58,rely=0.60)
win1=Tk()
win1.state('zoomed')
p1=ImageTk.PhotoImage(Image.open('sample1.png'))
l1=Label(image=p1)
l1.grid()
win1.after(8000,f1)
win1.config(bg='#ffdddd')
win1.mainloop()




















