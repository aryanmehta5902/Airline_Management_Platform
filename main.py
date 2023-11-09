from tkinter import *
from PIL import Image, ImageTk


root=Tk()



def search():
    uid1=str(uid.get())
    fn=str(fnn.get())
    ln=str(lnn.get())
    age1=int(agen.get())
    gender1=str(gendern.get())
    from1=str(ffrom.get())
    to1=str(tto.get())


#[6:20 pm, 01/04/2022] Aryan Mehta: %sql INSERT INTO searchbook1 (userid,fname,lname,age,gender,ffrom,fto) values (:uid1,:fn,:ln,:age1,:gender1,:from1,:to1);
#[6:27 pm, 01/04/2022] Aryan Mehta: %sql select * from flights1 where ffrom=:from1 and fto=:to1;\

def clearmain1():
    mainpage.grid_forget()
    bookbutton = Button(bookticket, text="SEARCH FLIGHTS!", padx=10, pady=10,command=search)
    bookbutton.grid(row=25, column=3)
    goback1=Button(bookticket,text="GO TO MAIN PAGE!",font="comicsansms 9",command=gomain1)
    goback1.grid(row=26,column=3,pady=15)
    bookticket.grid()

def clearmain2():
    mainpage.grid_forget()


def clearmain3():
    mainpage.grid_forget()



def gomain1():
    bookticket.grid_forget()
    mainpage.grid()



root.geometry("1000x1000")
root.title("AIRLINE MANAGEMENT SYSTEM")
root.wm_iconbitmap("flightlogo.ico")

titleframe=Frame(root,width=800,height=35)
img=Image.open("plane.jpg")
img=img.resize((200,150),Image.ANTIALIAS)
pht=ImageTk.PhotoImage(img)
Label(titleframe,image=pht,pady=10).grid(row=0,column=5,padx=30)
title=Label(titleframe,text="AIR LINE MANAGEMENT SYSTEM",font="comicsansms 20 bold underline",fg="white",bg="red",padx=220,pady=20)
title.grid(row=0,column=6)
titleframe.grid(row=0,column=0)

mainpage=Frame(root)
b1=Button(mainpage,text="PRESS HERE TO BOOK FLIGHT TICKET!    ",command=clearmain1,font="comicsansms 10 bold",padx=10,pady=50,borderwidth=5)
b2=Button(mainpage,text="PRESS HERE TO VIEW AVAILABLE FLIGHTS!",command=clearmain2,font="comicsansms 10 bold",padx=3,pady=50,borderwidth=5)
b3=Button(mainpage,text="PRESS HERE TO VIEW USERDATA!         ",command=clearmain3,font="comicsansms 10 bold",padx=17,pady=50,borderwidth=5)

b1.grid(column=10)
b2.grid(column=10)
b3.grid(column=10)
mainpage.grid()

uid=StringVar()
fnn=StringVar()
lnn=StringVar()
agen=StringVar()
gendern=StringVar()
ffrom=StringVar()
tto=StringVar()


bookticket=Frame(root)

e1=Entry(bookticket,textvariable=uid)
l1=Label(bookticket,text="ENTER USERID:")
l1.grid(row=5,column=2,pady=5,padx=10)
e1.grid(row=5,column=3,pady=5,padx=10)
e2=Entry(bookticket,textvariable=fnn)
l2=Label(bookticket,text="ENTER FIRSTNAME:")
l2.grid(row=6,column=2,pady=5,padx=10)
e2.grid(row=6,column=3,pady=5,padx=10)
e3=Entry(bookticket,textvariable=lnn)
l3=Label(bookticket,text="ENTER LASTNAME:")
l3.grid(row=7,column=2,pady=5,padx=10)
e3.grid(row=7,column=3,pady=5,padx=10)
e4=Entry(bookticket,textvariable=agen)
l4=Label(bookticket,text="ENTER AGE:")
l4.grid(row=8,column=2,pady=5,padx=10)
e4.grid(row=8,column=3,pady=5,padx=10)
e5=Entry(bookticket,textvariable=gendern)
l5=Label(bookticket,text="ENTER GENDER:")
l5.grid(row=9,column=2,pady=5,padx=10)
e5.grid(row=9,column=3,pady=5,padx=10)
e6=Entry(bookticket,textvariable=ffrom)
l6=Label(bookticket,text="ENTER FROM WHERE YOU WANT BOARD:")
l6.grid(row=10,column=2,pady=5,padx=10)
e6.grid(row=10,column=3,pady=5,padx=10)
e7=Entry(bookticket,textvariable=tto)
l7=Label(bookticket,text="ENTER WHERE YOU WANT TO REACH:")
l7.grid(row=11,column=2,pady=5,padx=10)
e7.grid(row=11,column=3,pady=5,padx=10)










root.mainloop()
