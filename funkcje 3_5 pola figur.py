# funkcja liczaca pola figur
# kwadrat
# prostokat
# trapez
# trójkąt
# kolo

import math


def pole(figura, podst=0, podst2=0, wys=0, r=0):
    if figura == 'kwadrat':
        return podst ** 2
    elif figura == 'prostokąt':
        return podst * wys
    elif figura == 'trapez':
        return (podst + podst2) * wys / 2
    elif figura == 'trójkąt':
        return podst * wys / 2
    elif figura == 'koło':
        return math.pi * r ** 2
    else:
        return -1


def test_kwadrat():
    assert pole('kwadrat', podst=4) == 16


def test_prostokat():
    assert pole('prostokąt', podst=5, wys=7) == 35


def test_trapez():
    assert pole('trapez', 2, 3, 4) == 10


def test_trojkat():
    assert pole('trójkąt', 7, wys=5) == 17.5


def test_kolo():
    assert round(pole('koło', r=1), 2) == 3.14
