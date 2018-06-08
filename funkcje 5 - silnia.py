# fukcja może wywołać inną funkcję

def dodaj(x,y):
    return x+y

def mnożenie(a,b):
    wynik = 0
    for i in range(a):
        wynik = dodaj(wynik, b)
    return wynik

print(mnożenie(6,5))

# rekurencja
def silnia(liczba):
    # warunek stopu!
    if liczba < 0:
        return None
    if liczba == 0 or liczba == 1:
        return 1
    #wywołanie rekurencyjne
    wynik = liczba * silnia(liczba-1)
    return wynik

print(silnia(998))