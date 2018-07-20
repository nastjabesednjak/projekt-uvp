from tkinter import *
import tkinter.messagebox
import os
import random

class Parametri:
    def __init__(self):
        pass
    x1 = 55
    x2 = 30
    y1 = 50
    y2 = 25
    poskus = 0
    tezavnost = 6
    tezavnost_raw = 6

parametri = Parametri

class Barve:
    def __init__(self):
        self.barve = [0,0,0,0]

    @property
    def generator_barv(self):               #Naključno izbere barve, ki jih igralec išče.

        index = 1
        self.barve[0] = random.randint(1, 6)

        izbrane_barve = [self.barve[0], 0, 0, 0]

        while index < 4:
            self.barve[index] = random.randint(1, 6)
            if self.barve[index] not in izbrane_barve:
                izbrane_barve[index] = self.barve[index]
                index += 1
        return izbrane_barve

    @generator_barv.setter                  #Izbiro generatorja shrani v "barve".
    def generator_barv(self, izbrane_barve):
        self.barve = izbrane_barve

izbira = Barve()
izbira.barve = izbira.generator_barv

class Vnos:
    def __init__(self):
        self.vnos = [0,0,0,0]

    def ugibanje(self, barva):    # Igralčevo barvo vnese na posamezno mesto v vrstici ugibanja.

        self.barva = barva

        if self.vnos[0] == 0:
            self.vnos[0] = self.barva
        elif self.vnos[1] == 0:
            self.vnos[1] = self.barva
        elif self.vnos[2] == 0:
            self.vnos[2] = self.barva
        elif self.vnos[3] == 0:
            self.vnos[3] = self.barva
            primerjava_resitve(izbira.barve, self.vnos)
        else:
            self.vnos = [0, 0, 0, 0,]  # Če so vse barve enega poskusa izbrane, se funkcija ponastavi in se ponovno izvede
            self.vnos[0] = self.barva

vnos = Vnos()

def SpawnKrog(barva, poskus, tezavnost, x1, x2, y1, y2):

    if tezavnost != 0:
        if poskus <= 2:             #Izriše kroge na pozicijah 0, 1, 2
            parametri.x1 += 30
            parametri.x2 += 30
            polje_krogi.create_oval(x1, y1,x2, y2, fill=barva)
            parametri.poskus += 1

        else:                           #Nariše zadnji krog na poziciji 3
            parametri.x1 = 55
            parametri.x2 = 30
            parametri.y1 += 30
            parametri.y2 += 30
            polje_krogi.create_oval(x1, y1, x2, y2, fill=barva)
            parametri.poskus = 0

            parametri.tezavnost -= 1

    slovar_stevk = {"blue" : 1, "red" : 2, "yellow" : 3,"green" : 4,"purple" : 5, "orange" : 6}
    vnos.ugibanje(slovar_stevk.get(barva))

def primerjava_resitve(barve, vnos):

    i = 0
    prikaz = [0, 0, 0, 0]
    for n in barve:
        if n in vnos:
            if vnos[i] == n:
                prikaz[i] = 2
            else:
                prikaz[i] = 1
        else:
            prikaz[i] = 0
        i += 1

    izpis_primerjave(prikaz, parametri.y1-30, parametri.y2-30)
    konec_poskusa(vnos, barve, parametri.tezavnost)

def izpis_primerjave(prikaz, y1, y2):

    x3 = 25
    x4 = 0
    pravilno_mesto_barva = prikaz.count(2)
    pravilna_barva = prikaz.count(1)
    #print(prikaz)

    while pravilno_mesto_barva > 0:
        x3 += 30
        x4 += 30
        polje_preverjanje.create_oval(x3, y1, x4, y2, fill="black")
        pravilno_mesto_barva -= 1

    while pravilna_barva > 0:
        x3 += 30
        x4 += 30
        polje_preverjanje.create_oval(x3, y1, x4, y2)
        pravilna_barva -= 1

def pravilna_resitev(resitev):

    x5 = 175
    x6 = 150

    slovar_barv = {1 : "blue", 2 : "red", 3 : "yellow", 4 : "green", 5 : "purple", 6 : "orange"}

    for stevilka_barve in resitev:
        polje_resitev.create_oval(x5, 50, x6, 25, fill=slovar_barv.get(stevilka_barve))
        x5 += 30
        x6 += 30

def konec_poskusa(vnos, barve, tezavnost):      # Ko igralec ugotovi pravilno rešitev ali uporabi vse poiskuse,
                                                # se mu prikaže pravilna rešitev in
                                                # okno s čestitkami ali "poskusite ponovno".
    if vnos == barve:
        tezavnost = 0
        pravilna_resitev(barve)
        tkinter.messagebox.showinfo("Memo", "Čestitam, našli ste pravilno rešitev!")
    elif tezavnost != 0:
        None
    else:
        pravilna_resitev(barve)
        tkinter.messagebox.showinfo("Memo", "Poskusite ponovno.")

def nova_igra():

    polje_krogi.delete(ALL)
    polje_preverjanje.delete(ALL)
    polje_resitev.delete(ALL)

    parametri.poskus = 0
    parametri.tezavnost = parametri.tezavnost_raw

    vnos.vnos = [0, 0, 0, 0]

    parametri.x1 = 55
    parametri.x2 = 30
    parametri.y1 = 50
    parametri.y2 = 25

    izbira.barve = izbira.generator_barv

def srednja_tezavnost():

    parametri.tezavnost_raw = 6
    nova_igra()

#Določi težjo težavnostno stopnjo s petimi mogočimi poskusi
def tezja_tezavnost():

    parametri.tezavnost_raw = 5
    nova_igra()

#Določi lažjo težavnostno stopnjo s sedmimi mogočimi poskusi
def lahka_tezavnost():

    parametri.tezavnost_raw = 7
    nova_igra()

def pravila():
    os.startfile("Pravila")

okno = Tk()

okvir_barve = Frame(okno)
okvir_barve.pack()

moder_gumb = Button(okvir_barve, text='Modra', bg="blue", fg="white", command = lambda : SpawnKrog("blue", parametri.poskus, parametri.tezavnost, parametri.x1, parametri.x2, parametri.y1, parametri.y2))
rumen_gumb = Button(okvir_barve, text='Rumena', bg="yellow", command = lambda : SpawnKrog("yellow", parametri.poskus, parametri.tezavnost, parametri.x1, parametri.x2, parametri.y1, parametri.y2))
rdec_gumb = Button(okvir_barve, text='Rdeča', bg="red", command = lambda : SpawnKrog("red", parametri.poskus, parametri.tezavnost, parametri.x1, parametri.x2, parametri.y1, parametri.y2))
zelen_gumb = Button(okvir_barve, text='Zelena', bg="green", command = lambda : SpawnKrog("green", parametri.poskus, parametri.tezavnost, parametri.x1, parametri.x2, parametri.y1, parametri.y2))
oranzen_gumb = Button(okvir_barve, text='Oranžna', bg="orange", command = lambda : SpawnKrog("orange", parametri.poskus, parametri.tezavnost, parametri.x1, parametri.x2, parametri.y1, parametri.y2))
vijola_gumb = Button(okvir_barve, text='Vijola', bg="purple", fg="white", command = lambda : SpawnKrog("purple", parametri.poskus, parametri.tezavnost, parametri.x1, parametri.x2, parametri.y1, parametri.y2))

moder_gumb.pack(side=LEFT)
rdec_gumb.pack(side=LEFT)
rumen_gumb.pack(side=LEFT)
zelen_gumb.pack(side=LEFT)
vijola_gumb.pack(side=LEFT)
oranzen_gumb.pack(side=LEFT)

menu = Menu(okno)
okno.config(menu=menu)

pod_menu = Menu(menu)
menu.add_cascade(label='Meni', menu=pod_menu)
pod_menu.add_command(label='Nova igra', command=nova_igra)
pod_menu.add_command(label='Pravila', command=pravila)
pod_menu.add_separator()
pod_menu.add_command(label='Izhod', command=okno.destroy)

pod_menu_2 = Menu(menu)
menu.add_cascade(label='Težavnost', menu=pod_menu_2)
pod_menu_2.add_command(label='Lahko', command=lahka_tezavnost)
pod_menu_2.add_command(label='Srednje', command=srednja_tezavnost)
pod_menu_2.add_command(label='Težko', command=tezja_tezavnost)

igra_okvir = Frame(okno)
polje_krogi = Canvas(igra_okvir, width=200, height=300)
polje_preverjanje = Canvas(igra_okvir, width = 200, height = 300)

resitev_okvir = Frame(okno)
polje_resitev = Canvas(resitev_okvir, width=400, height=50)

resitev_okvir.pack(side=BOTTOM)
igra_okvir.pack(side=BOTTOM)
polje_krogi.pack(side = LEFT)
polje_preverjanje.pack(side = RIGHT)
polje_resitev.pack(side = BOTTOM)

okno.mainloop()
