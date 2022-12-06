dictionary={'A':'.-', 'B':'-...',
            'C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....',
            'I':'..', 'J':'.---', 'K':'-.-','L':'.-..', 'M':'--', 'N':'-.',
            'O':'---', 'P':'.--.', 'Q':'--.-','R':'.-.', 'S':'...', 'T':'-',
            'U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..',}

dictionary2={'.-':'A','-...':'B','-.-.':'C','-..':'D', '.':'E','..-.':'F','--.':'G','....':'H',
             '..':'I','.---':'J', '-.-':'K','.-..':'L', '--':'M', '-.':'N',
             '---':'O', '.--.':'P', '--.-':'Q','.-.':'R', '...':'S', '-':'T',
             '..-':'U', '...-':'V', '.--':'W','-..-':'X', '-.--':'Y', '--..':'Z',}


for i in range(500):
    d=int(input("1-zašifrovat 2=odšifrovat"))
    a=input("Zadaj vec na šifrovanie")
    a=a.upper()

    sifra=""




    if d==1: # šifrování

        void=" "
        for i in a: #indexování
            if i != ' ':
                void+=dictionary[i]+" "
            else:

                void += ' '


        print(void)



    else: # dešifrování
        void = ""
        splitstring = a.split(" ") #rozdělení
        for i in splitstring: #indexování
            void += dictionary2[i]