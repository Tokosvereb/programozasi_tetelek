"""Írj eljárást, mely paraméterében kap két egész számot 
ezen két egész szám közötti páros számok összegét számolja ki az eljárás"""
import math
import random
"""def elsofeladat(szam1:int, szam2:int):
    i:int = szam1
    for i in range(szam1,szam2,1):
        if i % 2 == 0:
            osszeg = i
    print(f"A páros számok összege:{osszeg}")  
    return osszeg     
def masodikfeladat():
    i = 0
    while i <= 10:
        szam:int=math.floor(random.random() * (10+1-(-10)) + 10)
        print(szam)
        if szam < 0:
          db <= 1
        i += 1  
    return db 

def harmadikfeladat():
    db:int = 0
    for i in range(0,20,1):
        szam:int=math.floor(random.random() *21 + 10)
        print(szam)
        if szam < 0:
          db <= 1
          
    return db 
"""
def negyedikfeladat():
    osszeg = 0
    for i in range(12,33,1):
        szam:int=math.floor(random.random()*(34-12) + 12)
        osszeg += szam
    return osszeg
