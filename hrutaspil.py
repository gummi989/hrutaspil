import random
import math
import time
#Gudmundur Natan Hardarson
#Dagsetning 4/23/2018

class Hrutar:
    def __init__(self,nafn ,thyngs, mjolk, ull, fjoldiafkvaema,einkunnlaeris,frjosemi, gerd, malir ):
        self.nafn = nafn
        self.thyngd
        self.mjolk
        self.ull
        self.fjoldiafkvaema
        self.einkunnlaeris
        self.frjosemi
        self.gerd
        self.malir

    def Lysing(self):
        print('Nafn:' ,self.nöfn)
        print('Þyngd:' ,self.þyngd)
        print('Mjólk:' ,self.mjólk)
        print('Ull:' ,self.ull)
        print('Fjöldafkvæma:' ,self.fjöldiafkvæma)
        print('Einkunnalæris:' ,self.einkunnlæris)
        print('Frjósemi:', self.frjósemi)
        print('Gerð:', self.gerð)
        print('Malir', self.malir)

spilari1 = []
spilari2 = []
on = True
while on:
    ollspil = []
    spilar1 = []
    spilari2 = []
    skra = open('hrutaspil.txt', 'r')
    for lina in skra:
        spil.append(lina)
skra.close()
temp = []
spilastokkur=[]

for stak in spil:
    temp = stak.split(",")
    splitstokkur.append(Hrutar(temp[0], temp[1], temp[2], temp[3], temp[4], temp[5], temp[6], temp[7], temp[8]))

























