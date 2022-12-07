dec = int(input("Zadejte kladné číslo v desítkové soustavě: "))

bin = bin(dec)
hex = hex(dec)
oct = oct(dec)

if(dec >0):
    print("Dvojková soustava: " + bin)
    print("Šestnáctková soustava: " + hex)
    print("Osmičková soustava: " + oct)

else:
    print("Číslo musí být kladné!")
