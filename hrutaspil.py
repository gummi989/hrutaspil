
#Gu�mundur Natan Har�arson
#Forritun
#26.04.2018

import random
import time

class Hrutar:
    def __init__(self,nafn,thyngd,mjolk,ull,afkvaemi,laeri,frjo,bak,malir):

        self.nafn = nafn
        #skilgreini self.nafn sem nafn
        self.thyngd = thyngd
        #skilgreini self.thyngd sem thyngd
        self.mjolk = mjolk
        #skilgreini self.mjolk sem mjolk
        self.ull = ull
        self.afkvaemi = afkvaemi
        #skilgreini self.ull sem ull
        self.laeri = laeri
        #skilgreini self.laeri sem laeri
        self.frjo = frjo
        #skilgreini self.frjo sem frjo
        self.bak = bak
        #skilgreini self.bak sem bak
        self.malir = malir
        #skilgreini self.malir sem malir


spil = []
skra =open("hrutaspil.txt", "r")
for lina in skra:
    spil.append(lina)
skra.close()
temp =[]
spilastokkur=[]

for stak in spil:
    temp = stak.split(",")
    spilastokkur.append(Hrutar(temp[0], temp[1], temp[2], temp[3],temp[4],temp[5],temp[6],temp[7],temp[8]))

random.shuffle(spilastokkur)
notandi =[]
tolva =[]
for x in range(26):
    notandi.append(spilastokkur[x])
for x in range(26,52):
    tolva.append(spilastokkur[x])


print("Spil notanda")
print("Nafn:", notandi[0].nafn)
print("1.Þyngd", notandi[0].thyngd)
print("2.Mjólk", notandi[0].mjolk)
print("3.Ull", notandi[0].ull)
print("4.Afkvæmi", notandi[0].afkvaemi)
print("5.Læri", notandi[0].laeri)
print("6.Frjó", notandi[0].frjo)
print("7.Bak", notandi[0].bak)
print("8.Malir", notandi[0].malir)
valNot = int(input("Veldu"))

if valNot == 1:
    val = "thyngd"
elif val
    
if notandi[0].val > tolva[0].val:


























