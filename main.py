"""
Závěrečný projekt z předmětu AP1VS.
Skupina: ST1416
Projekt: Trojuhelnik
Autori: Martin Žůrek, David Fiala, David Tomeček, Josef Kužel, David Žídek
 .. include:: README.md
"""
#Importuje knihovnu pro umožnění uspání kódu na určitý čas
import time

#V následujícím bloku zadá uživatel souřadnice pro body A, B, C
#nadefinování proměnných pro jednotlivé body a výpis dotazu na zadání hodnot uživatelem
aX = float(input("Enter the x coordinate for point A: "))
aY = float(input("Enter the y coordinate for point A: "))
bX = float(input("Enter the x coordinate for point B: "))
bY = float(input("Enter the y coordinate for point B: "))
cX = float(input("Enter the x coordinate for point C: "))
cY = float(input("Enter the y coordinate for point C: "))

#Zadané souřadnice bodů se uživateli vypíší na konzoli
print()
print("Bod A = [%.1f, %.1f]" %(aX, aY))
print("Bod B = [%.1f, %.1f]" %(bX, bY))
print("Bod C = [%.1f, %.1f]" %(cX, cY))

time.sleep(2) #waitTime 2 sekundy
print( )

#V tomto bloku se uživateli ukáží vypočítané strany troujúhelníku
print("Výpočet délky jednotlivých stran trojúhelníku ABC:")
#početní operace pro výpočet délky každé strany strojúhelníku
stranaA = numpy.sqrt(pow(bX - aX, 2) + pow(bY - aY, 2))
stranaB = numpy.sqrt(pow(cX - bX, 2) + pow(cY - bY, 2))
stranaC = numpy.sqrt(pow(aX - cX, 2) + pow(aY - cY, 2))
#výpis vypočtených délek stran
print("Délka strany a = %.1f cm." %stranaA)
print("Délka strany b = %.1f cm." %stranaB)
print("Délka strany c = %.1f cm." %stranaC)

time.sleep(2) #waitTime 2 sekundy
print( )

#V tomto bloku se ukáže vypočítaný obvod troujúhelníku
print("Výpočet obvodu trojúhelníku ABC:")
#vzorec pro výpočet obvodu trojúhelníku
obvod = stranaA + stranaB + stranaC
#výpis výsledku (hodnoty) obvodu
print("Trojúhelník ABC má obvod = %.1f cm." %obvod)

time.sleep(2) #waitTime 2 sekundy
print( )

#V tomto bloku se uživateli ukáže vypočítaný obsah zadaného trojúhelníku
print("Výpočet obsahu trojúhelníku ABC:")
#vzorec pro výpočet obsahu trojúhelníku
s = (stranaA + stranaB + stranaC) / 2
obsah = numpy.sqrt(s * (s - stranaA) * (s - stranaB) * (s - stranaC))
#výpis velikosti obsahu
print("Trojúhelník ABC má obsah = %.1f cm2." %obsah)

time.sleep(2) #waitTime 2 sekundy
print( )

#V tomto bloku se uživateli zobrazí zda je vůbec možné trojúhelník sestrojit
print("Ověření sestrojitelnosti trojúhelníku ABC:")
#podmínka IF se vzorci pro ověření zda-li lze trojúhelník ABC sestrojit
if ((stranaA + stranaB > stranaC) and
    (stranaB + stranaC > stranaA) and
    (stranaC + stranaA > stranaB)):
    print("Trojúhelník ABC lze sestrojit.")
else:
    print("Trojúhelník ABC nelze sestrojit.")

time.sleep(2) #waitTime 2 sekundy
print( )

#Poslední věc co se uživateli ukáže je ověření, zda je trojúhelník pravoúhlý
print("Ověření pravoúhlosti trojúhelníku ABC:")
#podmínka IF se vzorci pro ověření pravoúhlosti trojúhelníku
if ((pow(stranaA, 2) + pow(stranaB, 2) == pow(stranaC, 2)) or
    (pow(stranaB, 2) + pow(stranaC, 2) == pow(stranaA, 2)) or
    (pow(stranaC, 2) + pow(stranaA, 2) == pow(stranaB, 2))):
    print("Trojúhelník ABC je pravoúhlý.")
else:
    print("Trojúhelník ABC není pravoúhlý.")
