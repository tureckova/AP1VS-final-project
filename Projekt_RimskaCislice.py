""".

@mainpage
@brief Prevod z arabskych cisel na rimska cisla
@author Do, Janostik, Lunga, Blaho
"""


"""
Seznam zakladni rimskych cisel.
I	V	X	L	C	D	M
1	5	10	50	100	500	1000
"""


def tisice(cislo):
    """Zjisteni tisice.

    >>> tisice(3888)
    'MMM'
    """
    t = ["", "M", "MM", "MMM"]  # index v poli zacina s hodnotou 0
    if isinstance(cislo, str) or isinstance(cislo, float):
        raise TypeError("Nelze prevodit")
    tisic = t[cislo // 1000]  # 3888 // 1000 == 3
    return tisic  # znak na (3+1) pozici
