from tkinter import Entry, Label, StringVar
from tkinter.constants import CENTER
from fonction import *
def hill_cryptage1(text,DM1,DM2,DM3,DM4,self):
    x=text.get()
    test_text=testalpha(x)
    l=[]
    l.append(DM1.get())
    l.append(DM2.get())
    l.append(DM3.get())
    l.append(DM4.get())
    test_M=True
    for i in range(4):
        if testN(l[i])==False:
            test_M=False
            break
        else:
            if l[i][0]=="-":
                l[i]=l[i][1:]
            l[i]=int(l[i])
    
    if test_text == False:
        Label(self, text="", bg="#00FFF0",fg="white", width=20,height=2).place(x=180,y=250)
        error = Label(self,text='la message comporte aux moin un lettre alphabetique ', bg="#00FFF0",fg="red", font=("Courier", 10 ,"bold"))
        error.place(x=40,y=40)
        self.after(2000, error.destroy)
    elif test_M == False :
        Label(self, text="", bg="#00FFF0",fg="white", width=20,height=2).place(x=180,y=250)
        error = Label(self,text='les nombre de matrice doit etre des entier et non vide', bg="#00FFF0",fg="red", font=("Courier", 10 ,"bold"))
        error.place(x=15,y=105)
        self.after(2000, error.destroy)
    else:
        M=saisirMatrice(2,l)
        z=cryptage3(x,M)
        v=StringVar()
        v.set(z)
        Entry(self,textvariable=v , width=22,justify=CENTER,bg="red",fg='black').place(x=180,y=250)
        #Label(self, text=z, bg="black",fg="red", width=20,height=2).place(x=180,y=250)

def hill_decryptage1(text,DM1,DM2,DM3,DM4,self):
    x=text.get()
    test_text=testalpha(x)
    l=[]
    l.append(DM1.get())
    l.append(DM2.get())
    l.append(DM3.get())
    l.append(DM4.get())
    test_M=True
    for i in range(4):
        if testN(l[i])==False:
            test_M=False
            break
        else:
            if l[i][0]=="-":
                l[i]=l[i][1:]
            l[i]=int(l[i])
    
    if test_text == False:
        Label(self, text="", bg="#00FFF0",fg="white", width=20,height=2).place(x=180,y=250)
        error = Label(self,text='la message comporte aux moin un lettre alphabetique ', bg="#00FFF0",fg="red", font=("Courier", 10 ,"bold"))
        error.place(x=40,y=40)
        self.after(2000, error.destroy)
    elif test_M == False :
        Label(self, text="", bg="#00FFF0",fg="white", width=20,height=2).place(x=180,y=250)
        error = Label(self,text='les nombre de matrice doit etre des entier et non vide', bg="#00FFF0",fg="red", font=("Courier", 10 ,"bold"))
        error.place(x=15,y=105)
        self.after(2000, error.destroy)
    else:
        M=saisirMatrice(2,l)
        try:
            Minv=modMatInv(M,26)
            Minv=Minv.astype(int)
            z=cryptage3(x,Minv)
            v=StringVar()
            v.set(z)
            Entry(self,textvariable=v , width=22,justify=CENTER,bg="black",fg='red').place(x=180,y=250)
            #Label(self, text=z, bg="black",fg="white", width=20,height=2).place(x=180,y=250)
        except:
            Label(self, text="", bg="#00FFF0",fg="white", width=20,height=2).place(x=180,y=250)
            error = Label(self,text='!!!la matrice est non invercible ', bg="#00FFF0", font=("Courier", 10 ,"bold"))
            error.place(x=50,y=40)
            self.after(2000, error.destroy)

def hill_cryptage2(text,DM1,DM2,DM3,DM4,DM5,DM6,DM7,DM8,DM9,self):
    message=text.get()
    test_text=testalpha(message)
    l=[]
    l.append(DM1.get())
    l.append(DM2.get())
    l.append(DM3.get())
    l.append(DM4.get())
    l.append(DM5.get())
    l.append(DM6.get())
    l.append(DM7.get())
    l.append(DM8.get())
    l.append(DM9.get())
    test_M=True
    for i in range(9):
        if testN(l[i])==False:
            test_M=False
            break
        else:
            if l[i][0]=="-":
                l[i]=l[i][1:]
                l[i]=int(l[i])*(-1)
            else:
                l[i]=int(l[i])
    
    if test_text == False:
        error = Label(self,text='la message comporte aux moin un lettre alphabetique ', bg="#00FFF0",fg="red", font=("Courier", 10 ,"bold"))
        error.place(x=40,y=40)
        self.after(2000, error.destroy)
    elif test_M == False :
        error = Label(self,text='les nombre de matrice doit etre des entier et non vide', bg="#00FFF0",fg="red", font=("Courier", 10 ,"bold"))
        error.place(x=15,y=95)
        self.after(2000, error.destroy)
    else:
        M=saisirMatrice(3,l)
        z=cryptage3(message,M)
        v=StringVar()
        v.set(z)
        Entry(self,textvariable=v , width=22,justify=CENTER,bg="red",fg='black').place(x=180,y=270)
        #Label(self, text=z, bg="black",fg="white", width=20,height=2).place(x=180,y=270)

def hill_decryptage2(text,DM1,DM2,DM3,DM4,DM5,DM6,DM7,DM8,DM9,self):
    message=text.get()
    test_text=testalpha(message)
    l=[]
    l.append(DM1.get())
    l.append(DM2.get())
    l.append(DM3.get())
    l.append(DM4.get())
    l.append(DM5.get())
    l.append(DM6.get())
    l.append(DM7.get())
    l.append(DM8.get())
    l.append(DM9.get())
    test_M=True
    for i in range(9):
        if testN(l[i])==False:
            test_M=False
            break
        else:
            if l[i][0]=="-":
                l[i]=l[i][1:]
            l[i]=int(l[i])
    
    if test_text == False:
        error = Label(self,text='la message comporte aux moin un lettre alphabetique ', bg="#00FFF0",fg="red", font=("Courier", 10 ,"bold"))
        error.place(x=40,y=40)
        self.after(2000, error.destroy)
    elif test_M == False :
        error = Label(self,text='les nombre de matrice doit etre des entier et non vide', bg="#00FFF0",fg="red", font=("Courier", 10 ,"bold"))
        error.place(x=15,y=95)
        self.after(2000, error.destroy)
    else:
        M=saisirMatrice(3,l)
        try:
            Minv=modMatInv(M,26)
            Minv=Minv.astype(int)
            z=cryptage3(message,Minv)
            v=StringVar()
            v.set(z)
            Entry(self,textvariable=v , width=22,justify=CENTER,bg="black",fg='red').place(x=180,y=270)
            #Label(self, text=z, bg="black",fg="white", width=20,height=2).placeplace(x=180,y=270)
        except:
            Label(self, text="", bg="#00FFF0", width=20,height=2).place(x=180,y=270)
            error = Label(self,text='!!!la matrice est non invercible ', bg="#00FFF0", font=("Courier", 10 ,"italic"))
            error.place(x=30,y=40)
            self.after(2000, error.destroy)

def Resetvew(message,DM1,DM2,DM3,DM4,self):
    message.delete(0,'end')
    DM1.delete(0,'end')
    DM2.delete(0,'end')
    DM3.delete(0,'end')
    DM4.delete(0,'end')
    Label(self, text="    ", bg="#00FFF0",fg="white", width=20,height=2).place(x=180,y=250)

def Resetvew1(message,DM1,DM2,DM3,DM4,DM5,DM6,DM7,DM8,DM9,self):
    message.delete(0,'end')
    DM1.delete(0,'end')
    DM2.delete(0,'end')
    DM3.delete(0,'end')
    DM4.delete(0,'end')
    DM5.delete(0,'end')
    DM6.delete(0,'end')
    DM7.delete(0,'end')
    DM8.delete(0,'end')
    DM9.delete(0,'end')
    Label(self, text="    ", bg="#00FFF0",fg="white", width=20,height=2).place(x=180,y=270)
