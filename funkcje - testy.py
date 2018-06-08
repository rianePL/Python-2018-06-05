
# funkcja którą będziemy testować czy dobrze działa
def dodaj(a,b):
    return a + b


def test_dodaj():
    # przygotowanie środowiska
    liczba1 = 4
    liczba2 = 5

    # odpalenie funkcji którą chcemy przetestować
    wynik = dodaj(liczba1, liczba2)

    # sprawdzenie wyników
    assert wynik == 9

def test_nieudany():
    assert dodaj(3,5) == 9