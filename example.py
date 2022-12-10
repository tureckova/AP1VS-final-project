dictionary={'A':'.-', 'B':'-...',
            'C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....',
            'I':'..', 'J':'.---', 'K':'-.-','L':'.-..', 'M':'--', 'N':'-.',
            'O':'---', 'P':'.--.', 'Q':'--.-','R':'.-.', 'S':'...', 'T':'-',
            'U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..',}

dictionary2={'.-':'A','-...':'B','-.-.':'C','-..':'D', '.':'E','..-.':'F','--.':'G','....':'H',
             '..':'I','.---':'J', '-.-':'K','.-..':'L', '--':'M', '-.':'N',
             '---':'O', '.--.':'P', '--.-':'Q','.-.':'R', '...':'S', '-':'T',
             '..-':'U', '...-':'V', '.--':'W','-..-':'X', '-.--':'Y', '--..':'Z',}


def coding(s):
    void=" "
    for i in s: #indexování
        if i != ' ':
            void+=dictionary[i]+" "
        else:
            void += ' '

    print(void)

    
def decoding(s):
    void = ""
    splitstring = a.split(" ") #rozdělení podle mezer
    for i in splitstring: #indexování
            void += dictionary2[i]
    print(void)

c = 1
while(c!="0"):
    d=int(input("1. Z ČEŠTINY DO MORSEOVKY || 2. Z MORESOVKY DO ČEŠTINY ")) # menu
    a=input("ZADEJ TEXT NA ŠIFROVÁNÍ: ")
    a=a.upper()

    sifra="" # nevyužívá se ale bez ní program nelze spustit




    if d==1: # šifrování
        coding(a)



    else: # dešifrování
        decoding(a)

  
    c = input(("POKUD CHCTE PROGRAM UKONČIT, ZADEJTE 0 || PRO POKRAČOVÁNÍ ZADEJTE LIBOVOLNÝ ZNAK : "))