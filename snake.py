#Razred Polje:

#Razred polje je glavni razred v katerem se igrica igra
#hrani razred kača, trenuten rezultat, 2d numpy matriko in koordinato polja, na katerem je hrana
#razred polje  je tudi razred, ki spremlja kaj uporabnik piše v konzolo
#razred polje hrani igralno polje kot 2d numpy matriko; vse kordinate so koordinate v tej matriki
#razred polje skrbi za izris igralnega polja

#Razred Kača
#razred kača hrani vse koordinate na kateriih kača je, smer v katero kača gleda, in boolean ali je kača živa ali mrtva
#razred ima funkcijo, ki prejme smer in ko se funkcija izvede, kačo obrne v to smer (če jo lahko)
#razred ima tudi funkcijo, ki preveri, ali je kača pojedla samo sebe in ali se je kača zabila v steno
#razded ima funkcijo, ki celo kačo premakne za 1 polje v smer katero gleda -> POMEMBNO NARIŠI SI
#razred ima funkcijo, ki kačo podaljša za 1 polje če ta poje hrano (to ali poje hrano se lahko spremlja iz razreda polje)

#osveževanje zaslova;
#vse igrice imajo neko frekvenco osveževanja zaslona (FPS)
#sami določite frekvenco osveževanja, in med vsako osvežitvijo izvedite komando "cls" -> import os
#|_> za to obstajajo tudi druge opcije, če najdeš katero, jo lahko tudi uporabiš
#frekvenco osveževanje določimo s time.sleep() -> za to ne pozabi import time


#Kako se take stvari lotit?
#1. začnemo z razredom polje
#   -> najprej napišemo konstruktor (__init__) in določimo katere vse podatke bo razred potreboval (kaca, 2d numpy matrika itd)
#   -> napišemo funkcijo za izris (__str__) -> ne pozabi da je treba izrisati tudi kačo in hrano
#   -> dopolnimo funkcijo za izris, da kombiniramo s time.sleep in cls
#   -> najdemo način, da lahko sproti spremljamo vse kar uporabnik vnese v konzolo (kaj se piše na tipkovnici)

#2. nadaljujemo z razredom kača
#   -> najprej naredimo konstruktor
#   -> naredimo funkcijo, ki preveri čeje kača živa ali mrtva
#   -> naredimo funkcijo, ki prejme smer in kačo obrne v to smer, če je možno
#   -> naredimo funkcijo, ki kačo premakne za 1 polje v smer gledanja
#   -> naredimo funkcijo ki kačo podaljša za 1 polje -> to je v laho v isti funckiji kot premik, samo da ne zradiramo repa 

import numpy as np
import time
import os
import threading
import keyboard
import random



def naprintaj():
    polja=np.zeros((8, 8), dtype=object)
    for i in range(len(kaca.cord_x)):
        polja[kaca.cord_y[i]][kaca.cord_x[i]]='='
    polja[hrana.y][hrana.x]='X'
    print(polja)

def zivljenje():
    kaca.preveri()
    if kaca.life==0:
        return False
    else:
        return True
    
    

class Kaca:
    def __init__(self):
        self.life=1
        self.cord_x=[3]
        self.cord_y=[3]
        self.smer='dol'
        
    def levo(self):
        if self.cord_x[0]==0:
            self.cord_x.insert(0, 7)
        else:
            self.cord_x.insert(0, self.cord_x[0]-1)
        
        self.cord_y.insert(0, self.cord_y[0])
        
        if hrana.x==self.cord_x[0] and hrana.y==self.cord_y[0]:
            hrana.premakni()
        else:
            self.cord_x.pop()
            self.cord_y.pop()
        
    def desno(self):
        if self.cord_x[0]==7:
            self.cord_x.insert(0, 0)
        else:
            self.cord_x.insert(0, self.cord_x[0]+1)
        
        self.cord_y.insert(0, self.cord_y[0])
        
        if hrana.x==self.cord_x[0] and hrana.y==self.cord_y[0]:
            hrana.premakni()
        else:
            self.cord_x.pop()
            self.cord_y.pop()
        
    def gor(self):
        if self.cord_y[0]==0:
            self.cord_y.insert(0, 7)
        else:
            self.cord_y.insert(0, self.cord_y[0]-1)
        
        self.cord_x.insert(0, self.cord_x[0])
        
        if hrana.x==self.cord_x[0] and hrana.y==self.cord_y[0]:
            hrana.premakni()
        else:
            self.cord_x.pop()
            self.cord_y.pop()
        
    def dol(self):
        if self.cord_y[0]==7:
            self.cord_y.insert(0, 0)
        else:
            self.cord_y.insert(0, self.cord_y[0]+1)
        
        self.cord_x.insert(0, self.cord_x[0])
        
        if hrana.x==self.cord_x[0] and hrana.y==self.cord_y[0]:
            hrana.premakni()
        else:
            self.cord_x.pop()
            self.cord_y.pop()
        
    def preveri(self):
        pass
        
class Hrana:
    def __init__(self):
        self.y=6
        self.x=6
    def premakni(self):
        neki_y=random.randint(0, 7)
        neki_x=random.randint(0, 7)
        for i in range(len(kaca.cord_x)):
            if neki_x==kaca.cord_x[i] and neki_y==kaca.cord_y[i]:
                hrana.premakni()
            else:
                self.x=neki_x
                self.y=neki_y
        
        
            
hrana=Hrana()        
kaca=Kaca()

def skeniraj():
    while True:
        if keyboard.is_pressed('w'):
            kaca.smer="gor"
        elif keyboard.is_pressed('a'):
            kaca.smer="levo"
        elif keyboard.is_pressed('s'):
            kaca.smer="dol"
        elif keyboard.is_pressed('d'):
            kaca.smer="desno"

def premakni():
    if kaca.smer=='gor':
        kaca.gor()
    elif kaca.smer=='dol':
        kaca.dol()
    elif kaca.smer=='levo':
        kaca.levo()
    elif kaca.smer=='desno':
        kaca.desno()

threading.Thread(target=skeniraj, daemon=True).start()



while zivljenje():
    time.sleep(0.3)
    os.system('cls')
    premakni()
    naprintaj()
    
    