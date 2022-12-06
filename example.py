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
    
    a=input("Zadaj vec na šifrovanie")
    a=a.upper()

    sifra=""



    d=int(input("1-zašifrovat 2=odšifrovat"))
    if d==1:
    
        void=" "
        for i in a:
            if i != ' ':
                void+=dictionary[i]+" "
            else:
        
                void += ' '


        print(void)


    
    else:
        void = ""
        splitstring = a.split(" ")
        for i in splitstring:
            void += dictionary2[i]

    
    
        print(void)