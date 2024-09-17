from tkinter import Entry, Label, StringVar
from tkinter.constants import CENTER
from fonction import *

def cae_cryptage(text,key,self):
    x=text.get()
    test_text=testalpha(x)
    y=key.get()
    test_key=testN(y)

    if test_text==False:
        Label(self, text="    ", bg="#00FFF0",fg="white", width=20,height=2).place(x=170,y=270)
        error = Label(self,text='la message comporte aux moin un lettre alphabetique', bg="#00FFF0",fg="red", font=("Courier", 10 ,"bold"))
        error.place(x=50,y=60)
        self.after(2000, error.destroy)
    elif test_key == False:
        Label(self, text="    ", bg="#00FFF0",fg="white", width=20,height=2).place(x=170,y=270)
        error = Label(self,text='Attention!!!!la clé doit étre un entier différent a 0', bg="#00FFF0", fg="red",font=("Courier", 10 ,"bold"))
        error.place(x=50,y=120)
        self.after(2000, error.destroy)
    else:
        if y[0]=='-':
            y=y[1:]
            y=int(y)*-1
            y=y%26
        else:
            y=int(y)
        z=crypter1(x,y)
        v=StringVar()
        v.set(z)
        Entry(self,textvariable=v , width=22,justify=CENTER,bg="red").place(x=170,y=270)
        #Label(self, text=z, bg="black",fg="red", width=20,height=2).place(x=170,y=270)
            

def cae_decryptage(text,key,self):
    x=text.get()
    test_text=testalpha(x)
    y=key.get()
    test_key=testN(y)

    if test_text==False:
        Label(self, text="    ", bg="#00FFF0",fg="white", width=20,height=2).place(x=170,y=270)
        error = Label(self,text='la message comporte aux moin un lettre alphabetique', bg="#00FFF0", fg="red",font=("Courier", 10 ,"bold"))
        error.place(x=50,y=60)
        self.after(4000, error.destroy)
    elif test_key == False:
        Label(self, text="    ", bg="#00FFF0",fg="white", width=20,height=2).place(x=170,y=270)
        error = Label(self,text='Attention!!!!la clé doit étre un entier différent a 0 ', bg="#00FFF0",fg="red", font=("Courier", 10 ,"bold"))
        error.place(x=50,y=120)
        self.after(4000, error.destroy)
    else:
        if y[0]=='-':
            y=y[1:]
            y=int(y)*-1
            y=y%26
        else:
            y=int(y)
        z=decrypter1(x,y)
        v=StringVar()
        v.set(z)
        Entry(self,textvariable=v , width=22,justify=CENTER,bg="black",fg="red").place(x=170,y=270)
        #Label(self, text=z, bg="black",fg="red", width=20,height=2).place(x=170,y=270)
def caesar_reset(message,key,self):
    message.delete(0,'end')
    key.delete(0,'end')
    Label(self, text="    ", bg="#00FFF0",fg="white", width=20,height=2).place(x=170,y=270)