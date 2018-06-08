def wiecej_niz(napis, licz_powt):
    # sprawdz wszystkie znaki w napisie
    # petla for
    # stworz slownik litera:liczba_wystapien

    znaki = {}
    zanki = {'a':2}
    for litera in napis:
        if litera in znaki:
            znaki[litera] += 1
        else:
            zanki[litera] = 1

    # wybierz te, które mają wartość > licz_powt
    # wrzuć je do zbioru
    # zwroc zbior

    wynik = set()
    for litera in znaki:
        if znaki[litera] > licz_powt:
            wynik.add(litera)

    return wynik

    # # pusty słownik
    # znaki = {}
    #
    # # wstawianie do słownika
    # znaki[litera] = 1
    #
    # # sprawdzenie czy jest w słowniku
    # if litera in znaki:
    #
    # # zwiększenie liczby wystapien
    # znaki[litera] = znaki[litera] + 1
    # znaki[litera] += 1
    #
    # # pusty zbior
    # wynik = set()
    #
    # # wstawianie do zbioru
    # wynik.add(litera)

print(wiecej_niz('ala ma kota a kot ma alę', 3))