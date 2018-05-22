from tkinter import *
import tkinter.messagebox
import os
import random

x1 = 25
x2 = 0
y1 = 50
y2 = 25

poskus = 0
tezavnost = 24
tezavnostRaw = 6
barva = "black"

barve = [0, 0, 0, 0]
vnos = [0, 0, 0, 0]
prikaz = [0, 0, 0, 0]
pravilno_mesto_barva = 0
pravilna_barva = 0

# Računalnik naključno izbere 4 izmed 6 barv
def izbira():
    global barve

    index = 1
    barve[0] = random.randint(1, 6)

    izbrane_barve = [barve[0], 0, 0, 0]

    while index < 4:
        barve[index] = random.randint(1, 6)
        if barve[index] not in izbrane_barve:
            izbrane_barve[index] = barve[index]
            index += 1

izbira()

#Ob koncu igre se prikaže pravilna rešitev
def pravilna_resitev(resitev):
    global barva

    x5 = 175
    x6 = 150
    y3 = 50
    y4 = 25

    for stevilka_barve in resitev:
        if stevilka_barve == 1:
            barva = "blue"
        elif stevilka_barve == 2:
            barva = "red"
        elif stevilka_barve == 3:
            barva = "yellow"
        elif stevilka_barve == 4:
            barva = "green"
        elif stevilka_barve == 5:
            barva = "purple"
        else:
            barva = "orange"

        polje_resitev.create_oval(x5, y3, x6, y4, fill=barva)
        x5 += 30
        x6 += 30

#Preveri igralčev poskus, če se ugibanje ujema z izbranimi barvammi
def preveri_poskus():
    global prikaz, pravilno_mesto_barva, pravilna_barva, y1, y2

    x3 = 25
    x4 = 0

    pravilno_mesto_barva = prikaz.count(2)
    pravilna_barva = prikaz.count(1)

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

def primerjava_resitev():
    global barve, vnos, prikaz

    if barve[0] in vnos:
        if vnos[0] == barve[0]:
            prikaz[0] = 2
        else:
            prikaz[0] = 1
    else:
        prikaz[0] = 0

    if barve[1] in vnos:
        if vnos[1] == barve[1]:
            prikaz[1] = 2

        else:
            prikaz[1] = 1
    else:
        prikaz[1] = 0

    if barve[2] in vnos:
        if vnos[2] == barve[2]:
            prikaz[2] = 2
        else:
            prikaz[2] = 1
    else:
        prikaz[2] = 0

    if barve[3] in vnos:
        if vnos[3] == barve[3]:
            prikaz[3] = 2
        else:
            prikaz[3] = 1
    else:
        prikaz[3] = 0

    preveri_poskus()
    konec_igre()

# Ko igralec ugotovi pravilno rešitev, ali uporabi vse poiskuse,
# se mu prikaže pravilna rešitev in
# okno s čestitkami ali "poskusite ponovno".
def konec_igre():
    global vnos, barve, poskus, tezavnost
    if vnos == barve:
        tezavnost = 0
        pravilna_resitev(barve)
        tkinter.messagebox.showinfo("Memo", "Čestitam, našli ste pravilno rešitev!")
    elif tezavnost != 0:
        None
    else:
        pravilna_resitev(barve)
        tkinter.messagebox.showinfo("Memo", "Poskusite ponovno.")

#Določi srednjo težavnostno stopnjo s šestimi mogočimi poskusi
def srednja_tezavnost():

    global tezavnostRaw
    tezavnostRaw = 6
    nova_igra()

#Določi težjo težavnostno stopnjo s petimi mogočimi poskusi
def tezja_tezavnost():

    global tezavnostRaw
    tezavnostRaw = 5
    nova_igra()

#Določi lažjo težavnostno stopnjo s sedmimi mogočimi poskusi
def lahka_tezavnost():

    global tezavnostRaw
    tezavnostRaw = 7
    nova_igra()

def ugibanje(barva):

    global vnos

    if vnos[0] == 0:
        vnos[0] = barva
    elif vnos[1] == 0:
        vnos[1] = barva
    elif vnos[2] == 0:
        vnos[2] = barva
    elif vnos[3] == 0:
        vnos[3] = barva
        primerjava_resitev()
    else:
        vnos = [0, 0, 0, 0,]
        ugibanje(barva)

#Funkcije z imeni barv posamezni številki priredijo določeno barvo
def modra():
    SpawnKrog("blue")
    ugibanje(1)

def rdeca():
    SpawnKrog("red")
    ugibanje(2)

def rumena():
    SpawnKrog("yellow")
    ugibanje(3)

def zelena():
    SpawnKrog("green")
    ugibanje(4)

def vijola():
    SpawnKrog("purple")
    ugibanje(5)

def oranzna():
    SpawnKrog("orange")
    ugibanje(6)

# Ob vsakem igralčevem kliku na barvo se izriše nov krog v izbravi barvi.
def SpawnKrog(barva):

    global x1, x2, y1, y2, poskus, tezavnost

    if tezavnost != 0:
        if poskus <= 3:
            x1 += 30
            x2 += 30
            polje_krogi.create_oval(x1, y1, x2, y2, fill=barva)
            poskus += 1

        else:
            x1 = 55
            x2 = 30
            y1 += 30
            y2 += 30

            polje_krogi.create_oval(x1, y1, x2, y2, fill=barva)
            poskus = 1

        tezavnost -= 1

def nova_igra():

    global tezavnost, tezavnostRaw, x1, x2, y1, y2, poskus, barve, vnos, prikaz, pravilno_mesto_barva, pravilna_barva
    polje_krogi.delete(ALL)
    polje_preverjanje.delete(ALL)
    polje_resitev.delete(ALL)
    tezavnost = tezavnostRaw * 4

    barve = [0, 0, 0, 0]
    vnos = [0, 0, 0, 0]
    prikaz = [0, 0, 0, 0]
    pravilno_mesto_barva = 0
    pravilna_barva = 0

    x1 = 25
    x2 = 0
    y1 = 50
    y2 = 25
    poskus = 0

    izbira()

def pravila():
    os.startfile("Pravila")

okno = Tk()

okvir_barve = Frame(okno)
okvir_barve.pack()

moder_gumb = Button(okvir_barve, text='Modra', bg="blue", fg="white", command = modra)
rumen_gumb = Button(okvir_barve, text='Rumena', bg="yellow", command = rumena)
rdec_gumb = Button(okvir_barve, text='Rdeča', bg="red", command = rdeca)
zelen_gumb = Button(okvir_barve, text='Zelena', bg="green", command = zelena)
oranzen_gumb = Button(okvir_barve, text='Oranžna', bg="orange", command = oranzna)
vijola_gumb = Button(okvir_barve, text='Vijola', bg="purple", fg="white", command = vijola)
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
pod_menu.add_cascade(label='Pravila', command=pravila)
pod_menu.add_separator()
pod_menu.add_command(label='Izhod', command=okno.destroy)

pod_menu_2 = Menu(menu)
menu.add_cascade(label='Težavnost', menu=pod_menu_2)
pod_menu_2.add_command(label='Lahko', command=lahka_tezavnost)
pod_menu_2.add_command(label='Srednje', command=srednja_tezavnost)
pod_menu_2.add_command(label='Težko', command=tezja_tezavnost)

resitev_okvir = Frame(okno)
igra_okvir = Frame(okno)
polje_resitev = Canvas(resitev_okvir, width=400, height=50)
polje_krogi = Canvas(igra_okvir, width=200, height=300)
resitev_okvir.pack(side=BOTTOM)
igra_okvir.pack(side=BOTTOM)
polje_preverjanje = Canvas(igra_okvir, width = 200, height = 300)
polje_krogi.pack(side = LEFT)
polje_preverjanje.pack(side = RIGHT)
polje_resitev.pack(side = BOTTOM)

okno.mainloop()
