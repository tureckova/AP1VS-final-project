﻿import numpy

#V následujícím bloku zadá uživatel hodnoty souřadnic pro body A,B,C
#nadefinování proměnných, výpis textu na konzoli
aX = float(input("Enter the x coordinate for point A: "))
aY = float(input("Enter the y coordinate for point A: "))
bX = float(input("Enter the x coordinate for point B: "))
bY = float(input("Enter the y coordinate for point B: "))
cX = float(input("Enter the x coordinate for point C: "))
cY = float(input("Enter the y coordinate for point C: "))

#Zadané souřadnice se uživateli postupně vypíší
#výpis hodnot na konzoli (hodnoty, které byly zadány uživatelem)
print()
print("Bod A = [%.1f, %.1f]" %(aX, aY))
print("Bod B = [%.1f, %.1f]" %(bX, bY))
print("Bod C = [%.1f, %.1f]" %(cX, cY))

time.sleep(2)#waitTime 2 sekundy

#Zde se uživateli ukáží vypočítané strany troujúhelníku
#výpis textu
print( )
print("Výpočet délky jednotlivých stran trojúhelníku ABC:")
#početní operace pro každou stranu (A,B,C)
stranaA = numpy.sqrt(pow(bX - aX, 2) + pow(bY - aY, 2))
stranaB = numpy.sqrt(pow(cX - bX, 2) + pow(cY - bY, 2))
stranaC = numpy.sqrt(pow(aX - cX, 2) + pow(aY - cY, 2))
#výpis vypočtených délek stran
print("Délka strany a = %.1f cm." %stranaA)
print("Délka strany b = %.1f cm." %stranaB)
print("Délka strany c = %.1f cm." %stranaC)

time.sleep(2)#waitTime 2 sekundy

#V tomto bloku se ukáže vypočítaný obvod troujúhelníku
#výpis textu
print( )
print("Výpočet obvodu trojúhelníku ABC:")
#výpočet obvodu Trojúhelníku
obvod = stranaA + stranaB + stranaC
#výpis výsledku
print("Trojúhelník ABC má obvod = %.1f cm." %obvod)

time.sleep(2)#waitTime 2 sekundy

#Uživateli se zde ukáže vypočítaný obsah zadaného trojúhelníku
#výpis textu
print( )
print("Výpočet obsahu trojúhelníku ABC:")
#výpočet obsahu Trojúhelníku
s = (stranaA + stranaB + stranaC) / 2
obsah = numpy.sqrt(s * (s - stranaA) * (s - stranaB) * (s - stranaC))
#výpis výsledku
print("Trojúhelník ABC má obsah = %.1f cm2." %obsah)

time.sleep(2)#waitTime 2 sekundy

#Uživateli se zobrazí zda je vůbec možné sestorjit trojúhelník
#výpis textu
print( )
print("Ověření sestrojitelnosti trojúhelníku ABC:")
#podmínka IF, ověření zda-li jde trojúhelník ABC sestrojit
if ((stranaA + stranaB > stranaC) and
    (stranaB + stranaC > stranaA) and
    (stranaC + stranaA > stranaB)):
    print("Trojúhelník ABC lze sestrojit.")
else:
    print("Trojúhelník ABC nelze sestrojit.")

time.sleep(2)#waitTime 2 sekundy

#Poslední věc co se uživateli ukáže je ověření, zda je trojúhelník pravoúhlý
#výpis textu
print( )
print("Ověření pravoúhlosti trojúhelníku ABC:")
#podmínka IF, ověření pravoúhlosti trojúhelníku ABC
if ((pow(stranaA, 2) + pow(stranaB, 2) == pow(stranaC, 2)) or
    (pow(stranaB, 2) + pow(stranaC, 2) == pow(stranaA, 2)) or
    (pow(stranaC, 2) + pow(stranaA, 2) == pow(stranaB, 2))):
    print("Trojúhelník ABC je pravoúhlý.")
else:
    print("Trojúhelník ABC není pravoúhlý.")
