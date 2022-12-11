import pyttsx3
import pyjokes

def speak(joke):
    print(joke)
    computer = pyttsx3.init()
    computer.setProperty("rate", 150)
    computer.say(joke)
    computer.runAndWait()

def main(game):
    while game:
        print("jakou kategorii vtipů chceš ?")
        print(" 1 - all \n" + " 2 - chuck\n" + " 3 - neutral")
        userInput = int(input())

        if userInput == 1:
            joke = pyjokes.get_joke(category="all")
            speak(joke)
            uI = input("další vtip ?  press any key => ANO, press N => NE\n")
            if uI.upper() == "N":
                game = False

                
        elif userInput == 2:
            joke = pyjokes.get_joke(category="chuck")
            speak(joke)
            uI = input("další vtip ?  press any key => ANO, press N => NE\n")
            if uI.upper() == "N":
                game = False
        elif userInput == 3:
            joke = pyjokes.get_joke(category="neutral")
            speak(joke)
            uI = input("další vtip ?  press any key => ANO, press N => NE\n")
            if uI.upper() == "N":
                game = False
        else:
            print("nezadal jsi číslo v rozmezí 1 - 3! ")

    print("Konec programu")

if __name__ == "__main__":
    main(True)