from tkinter import *
from tkinter import font
from sys import exit
from datetime import datetime
from Caesar import *
from Viginere import *
from Hill import *

class root(Tk):

    def __init__(self, *args,**kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title_font = font.Font(family='Helvetica', size=20, weight="bold", slant="italic")
        self.iconbitmap("Logo.ico")
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=10)
        container.grid_columnconfigure(0, weight=10)
        

        self.frames = {}
    
    
        for F in (Menu, Caesar, Viginere, Hill,Hill_Matrice_2,Hill_Matrice_3):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Menu")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        self.winfo_toplevel().title(page_name)

class Menu(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#00FFF0")
        label = Label(self, text="CHIFFREMENT DE MESSAGE", font=controller.title_font, bg="#00FFF0")
        label.pack(side="top", fill="x", pady=30)
        caes_but = Button(self, text="Chiffrement De Caesar",command=lambda: controller.show_frame("Caesar"),width=25, pady=15)
        vig_but = Button(self, text="Chiffrement De Viginere",command=lambda: controller.show_frame("Viginere"),width=25, pady=15)
        hill_but = Button(self, text="Chiffrement De Hill",command=lambda: controller.show_frame("Hill"),width=25, pady=15)
        caes_but.place(x=150,y=100)
        vig_but.place(x=150,y=170)
        hill_but.place(x=150,y=240)
        Button(self, text="Quitter",command=exit).place(x=210,y=310)
       # Label(self,text=datetime.now(),font=("Courier", 8 ,"bold"), bg="#00FFF0").place(x=10,y=310)

class Caesar(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#00FFF0")

        label = Label(self, text="Caesar", font=controller.title_font, bg="#00FFF0")
        label.pack(side="top", fill="x", pady=10)
        
        Button(self, text="<<-Menu",command=lambda: controller.show_frame("Menu")).place(x=215,y=320)
        Label(self, text="Message", bg="#00FFF0").place(x=80,y=100)
        message = Entry(self, width=30)
        message.place(x=150,y=100)
        Label(self, text="Clé", bg="#00FFF0").place(x=100,y=150)
        key = Entry(self, width=30)
        key.place(x=150,y=150)
        enc_but = Button(self, text="Cryptage", padx=50,pady=10, command=lambda: cae_cryptage(message,key,self), bg="#b0b0b0", fg="black",)
        enc_but.place(x=80,y=200)
        dec_but = Button(self, text="Decryptage", padx=50,pady=10, command=lambda: cae_decryptage(message,key,self), bg="#b0b0b0", fg="black")
        dec_but.place(x=260,y=200)
        Reset=Button(self, text="Reset",command=lambda: caesar_reset(message,key,self)).place(x=280,y=320)

class Viginere(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#00FFF0")

        label = Label(self, text="Viginere", font=controller.title_font, bg="#00FFF0")
        label.pack(side="top", fill="x", pady=10)

        Button(self, text="<<-Menu",command=lambda: controller.show_frame("Menu")).place(x=180,y=300)
        Label(self, text="Message", bg="#00FFF0").place(x=80,y=100)
        message = Entry(self, width=30)
        message.place(x=150,y=100)
        Label(self, text="Clé", bg="#00FFF0").place(x=100,y=150)
        key = Entry(self, width=30)
        key.place(x=150,y=150)
        enc_but = Button(self, text="Cryptage", padx=50,pady=10, command=lambda: vig_cryptage(message,key,self), bg="#b0b0b0", fg="black",)
        enc_but.place(x=80,y=200)
        dec_but = Button(self, text="Decryptage", padx=50,pady=10, command=lambda: vig_decryptage(message,key,self), bg="#b0b0b0", fg="black")
        dec_but.place(x=260,y=200)
        Reset=Button(self, text="Reset",command=lambda: vig_reset(message,key,self)).place(x=250,y=300)

class Hill(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#00FFF0")

        label = Label(self, text="Hill", font=controller.title_font, bg="#00FFF0")
        label.pack(side="top", fill="x", pady=5)

        Label(self, text="Choisire le chiffremet avec un matrice 2X2 ou 3X3 !!", bg="#00FFF0",font=("Times", 15 ,"italic","bold")).place(x=30,y=100)

        Button(self, text="<<-Menu",command=lambda: controller.show_frame("Menu")).place(x=215,y=300)
        Button(self, text="Matrice 2X2", padx=50,pady=20, command=lambda:controller.show_frame("Hill_Matrice_2") ).place(x=50,y=200)
        Button(self, text="Matrice 3X3", padx=50,pady=20, command=lambda:controller.show_frame("Hill_Matrice_3") ).place(x=280,y=200)

class Hill_Matrice_2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#00FFF0")

        label = Label(self, text="Hill Avec Matrice 2X2", font=controller.title_font, bg="#00FFF0")
        label.pack(side="top", fill="x", pady=5)


        Label(self, text="Message:", bg="#00FFF0").place(x=80,y=80)
        message = Entry(self, width=30)
        message.place(x=150,y=80)
        Label(self, text="Matrice:", bg="#00FFF0").place(x=80,y=130)
        DM1= Entry(self, width=5)
        DM1.place(x=150,y=130)
        DM2= Entry(self, width=5)
        DM2.place(x=200,y=130)
        DM3= Entry(self, width=5)
        DM3.place(x=150,y=160)
        DM4= Entry(self, width=5)
        DM4.place(x=200,y=160)
        enc_but = Button(self, text="Cryptage", padx=50,pady=10, command=lambda: hill_cryptage1(message,DM1,DM2,DM3,DM4,self), bg="#b0b0b0", fg="black")
        enc_but.place(x=80,y=200)
        dec_but = Button(self, text="Decryptage", padx=50,pady=10, command=lambda: hill_decryptage1(message,DM1,DM2,DM3,DM4,self), bg="#b0b0b0", fg="black")
        dec_but.place(x=250,y=200)
        Button(self, text="Menu",command=lambda: controller.show_frame("Menu")).place(x=200,y=300)
        Button(self, text="<--Back",command=lambda: controller.show_frame("Hill")).place(x=250,y=300)
        Reset=Button(self, text="Reset",command=lambda:Resetvew(message,DM1,DM2,DM3,DM4,self)).place(x=310,y=300)

class Hill_Matrice_3(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#00FFF0")
        label = Label(self, text="Hill Avec Matrice 3X3", font=controller.title_font, bg="#00FFF0")
        label.pack(side="top", fill="x", pady=5)

        Label(self, text="Message: ", bg="#00FFF0").place(x=80,y=70)
        message = Entry(self, width=30)
        message.place(x=150,y=70)

        DM1= Entry(self, width=5)
        DM1.place(x=150,y=120)


        DM2= Entry(self, width=5)
        DM2.place(x=225,y=120)

        DM3= Entry(self, width=5)
        DM3.place(x=300,y=120)
        
        DM4= Entry(self, width=5)
        DM4.place(x=150,y=150)
        
        DM5= Entry(self, width=5)
        DM5.place(x=225,y=150)
        
        DM6= Entry(self, width=5)
        DM6.place(x=300,y=150)
        
        DM7= Entry(self, width=5)
        DM7.place(x=150,y=180)
        
        DM8= Entry(self, width=5)
        DM8.place(x=225,y=180)

        DM9= Entry(self, width=5)
        DM9.place(x=300,y=180)

        enc_but = Button(self, text="Cryptage", padx=50,pady=10, command=lambda: hill_cryptage2(message,DM1,DM2,DM3,DM4,DM5,DM6,DM7,DM8,DM9,self), bg="#b0b0b0", fg="black")
        enc_but.place(x=80,y=220)
        dec_but = Button(self, text="Decryptage", padx=50,pady=10, command=lambda: hill_decryptage2(message,DM1,DM2,DM3,DM4,DM5,DM6,DM7,DM8,DM9,self), bg="#b0b0b0", fg="black")
        dec_but.place(x=250,y=220)
        Button(self, text="Menu",command=lambda: controller.show_frame("Menu")).place(x=200,y=310)
        Button(self, text="<--Back",command=lambda: controller.show_frame("Hill")).place(x=250,y=310)
        Reset=Button(self, text="Reset",command=lambda:Resetvew1(message,DM1,DM2,DM3,DM4,DM5,DM6,DM7,DM8,DM9,self)).place(x=320,y=310)

app = root()
app.geometry("500x350")
app.resizable(False, False)
app.mainloop()