from tkinter import Entry, Label, StringVar
from tkinter.constants import CENTER
from fonction import *

def vig_cryptage(text,key,self):
    x=text.get()
    test_text=testalpha(x)
    y=key.get()
    test_key=testAlphaKey(y)
    if test_text == False :
        Label(self, text="    ", bg="#00FFF0",fg="white", width=20,height=2).place(x=170,y=260)
        error = Label(self,text='la message comporte aux moin un lettre alphabetique ', bg="#00FFF0",fg="red", font=("Courier", 10 ,"bold"))
        error.place(x=40,y=60)
        self.after(2000, error.destroy)
    elif test_key == False:
        Label(self, text="    ", bg="#00FFF0",fg="white", width=20,height=2).place(x=170,y=260)
        error = Label(self,text='la clé doit etre alphabetique sans des cractére spécial & espace ', bg="#00FFF0",fg="red", font=("Courier",8,"bold"))
        error.place(x=20,y=120)
        self.after(2000, error.destroy)
    else:
        z=cryptage2(x,y)
        v=StringVar()
        v.set(z)
        Entry(self,textvariable=v , width=22,justify=CENTER,bg="red").place(x=170,y=260)
        #Label(self, text=z, bg="black",fg="white", width=20,height=2).place(x=170,y=260)


def vig_decryptage(text,key,self):
    x=text.get()
    test_text=testalpha(x)
    y=key.get()
    test_key=testAlphaKey(y)
    if test_text == False :
        Label(self, text="    ", bg="#00FFF0",fg="white", width=20,height=2).place(x=170,y=260)
        error = Label(self,text='la message comporte aux moin un lettre alphabetique ', bg="#00FFF0", fg="red",font=("Courier", 10 ,"bold"))
        error.place(x=40,y=60)
        self.after(3000, error.destroy)
    elif test_key == False:
        Label(self, text="    ", bg="#00FFF0",fg="white", width=20,height=2).place(x=170,y=260)
        error = Label(self,text='la clé doit etre alphabetique sans des cractére spécial & espace ',fg="red", bg="#00FFF0", font=("Courier",8,"bold"))
        error.place(x=20,y=120)
        self.after(3000, error.destroy)
    else:
        z=decryptage2(x,y)
        v=StringVar()
        v.set(z)
        Entry(self,textvariable=v , width=22,justify=CENTER,bg="black",fg='red').place(x=170,y=260)
        #Label(self, text=z, bg="black",fg="white", width=20,height=2).place(x=170,y=260)
def vig_reset(text,key,self):
    text.delete(0,'end')
    key.delete(0,'end')
    Label(self, text="    ", bg="#00FFF0",fg="white", width=20,height=2).place(x=170,y=260)