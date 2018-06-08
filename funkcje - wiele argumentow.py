# funkcja która przyjmuje wiele argumentów
# nie wiadomo ile

# np suma(1,1,25,5,6)

def wypisz_argumenty(*args, **kwargs):
    print(f'wszystkie argumenty pozycyjne {args}')
    print(f'wszystkie argumenty kluczowe {kwargs}')


wypisz_argumenty(3,'ala', 8.5, wys=5, szer=6)

def suma(*args, **kwargs):
    wynik = 0
    for arg in args:
        wynik += arg
    for et in kwargs:
        wynik += kwargs[et]
    return wynik

def test_pusty():
    assert suma() == 0

def test_jeden():
    assert suma(5) == 5

def test_wiele():
    assert suma(3,4,6,8.5) == 21.5

def test_nazwane():
    assert suma(2, drugi=3, trzeci=7.5) == 12.5
