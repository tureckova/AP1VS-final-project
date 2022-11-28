import tkinter
import math

canvas = tkinter.Canvas(height=700, width=700)
canvas.pack()


def trojuhelnik():
    """
    print("Zadej hodnotu pro bod A:")
    """
    global a_x
    global a_y
    a_x = 100
    a_y = 100
    """
    a_x=int(input("Hodnota bodu A pozice X"))
    a_y=int(input("Hodnota bodu A pozice Y"))
    print("Zadaj hodnotu pro bod B:")
    """
    global b_x
    global b_y
    b_x = 100
    b_y = 100
    """
    b_x=int(input("Hodnota bodu B pozice X"))
    b_y=int(input("Hodnota bodu B pozice Y"))
    print("Zadaj hodnotu pro bod C:")
    """
    global c_x
    global c_y
    c_x = 100
    c_y = 500
    """
    c_x=int(input("Hodnota bodu C pozice X"))
    c_y=int(input("Hodnota bodu C pozice Y"))
    """

    print("  ", "X", "   ", "Y")
    print("A", a_x, ",", a_y)
    print("B", b_x, ",", b_y)
    print("C", c_x, ",", c_y)


def vypocty():
    global strana_A
    strana_A = (((b_x - c_x) ** 2 + (b_y - c_y) ** 2) ** 0.5)
    strana_A = round(strana_A, 2)

    global strana_B
    strana_B = (((c_x - a_x) ** 2 + (c_y - a_y) ** 2) ** 0.5)
    strana_B = round(strana_B, 2)

    global strana_C
    strana_C = (((a_x - b_x) ** 2 + (a_y - b_y) ** 2) ** 0.5)
    strana_C = round(strana_C, 2)

    global obvod
    obvod = strana_A + strana_B + strana_C
    obvod = round(obvod, 2)
    print("Obvod Trojúhelníka je:", obvod, "cm")

    s = (obvod) / 2

    global obsah
    obsah = ((s * (s - strana_A) * (s - strana_B) * (s - strana_C)) ** 0.5)
    obsah = round(obsah, 2)
    print("Obsah Trojúhelníka je:", obsah, "cm²")

    if strana_A + strana_B > strana_C and strana_B + strana_C > strana_A and strana_A + strana_C > strana_B:
        print("Trojúhelník lze narýsovat.")
        print("Délka strany A:", strana_A, "\nDélka strany B:", strana_B, "\nDélka strany C:", strana_C)
    else:
        print("Trojúhelník nelze narýsovat.")

def kresba():
    canvas.create_line(a_x, a_y, b_x, b_y, c_x, c_y, a_x, a_y, fill="blue", width=5)
    canvas.create_text(50, 620, fill="darkblue", font="Times 10", text=("Obvod Trojúhelníka je:", obvod, "cm"), anchor="w")
    canvas.create_text(50, 635, fill="darkblue", font="Times 10", text=("Obsah Trojúhelníka je:", obsah, "cm²"), anchor="w")
    canvas.create_text(50, 680, fill="darkblue", font="Times 10", text=("Délka strany A:", strana_A), anchor="w")
    canvas.create_text(50, 695, fill="darkblue", font="Times 10", text=("Délka strany B:", strana_B), anchor="w")
    canvas.create_text(50, 710, fill="darkblue", font="Times 10", text=("Délka strany C:", strana_C), anchor="w")

def extra():
    if (strana_A*strana_A + strana_B*strana_B==strana_C*strana_C) or (strana_A*strana_A + strana_C*strana_C==strana_B*strana_B) or (strana_B*strana_B + strana_C*strana_C==strana_A*strana_A):
        canvas.create_text(50, 650, fill="darkblue", font="Times 10", text=("Trojuholnik je pravouhlý"), anchor="w")
    else:
        canvas.create_text(50, 650, fill="darkblue", font="Times 10", text=("Trojuholnik nie je pravouhlý"), anchor="w")

    if strana_A + strana_B > strana_C and strana_B + strana_C > strana_A and strana_A + strana_C > strana_B:
        canvas.create_text(50, 665, fill="darkblue", font="Times 10", text=("Trojuholnik lze narýsovat"), anchor="w")
    else:
        canvas.delete('all')
        canvas.create_text(350, 350, fill="red", font="Times 25", text=("Trojuholnik nelze narýsovat"), anchor="center")



trojuhelnik()
vypocty()
kresba()
extra()
canvas.mainloop()
