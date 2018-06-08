# wyrażenia listowe
# szybkie tworzenie potrzebnych nam struktur
# skrócone pętle

kwadraty = []
for x in range(1, 11):
    kwadraty.append(x ** 2)
print(kwadraty)

kwadraty_lista = [x ** 2 for x in range(1, 11)]
print(kwadraty_lista)

kwadraty_słownik = {x: x ** 2 for x in range(1, 11)}
print(kwadraty_słownik)

kwadraty_zbiór = {x ** 2 for x in range(1, 11)}
print(kwadraty_zbiór)

kwadraty_niespodzianka = (x ** 2 for x in range(1, 11))
print(kwadraty_niespodzianka)

użycie = [x for x in kwadraty_niespodzianka]
print(użycie)

kwadraty_krotka = tuple(x for x in range(1, 11))
print(kwadraty_krotka)

# W sesji interaktywnego srodowiska stwórz nastepujace struktury
# danych korzystajac ze skróconej wersji zapisu:
# - liste zawierajaca liczby zmiennoprzecinkowe od 0.0 do 1.0 z
# krokiem 0.1
# - zbiór tupli zawierajacych 3 elementy - dana liczbe, jej kwadrat i
# jej szescian - w przedziale od -10 do 10
# - słownik mapujacy napisy na ich długosc powstały ze zbioru
# napisów

lista = [x * 0.1 for x in range(1, 11)]
print(lista)

lista = [x / 10 for x in range(1, 11)]
print(lista)

jedynki = [0.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]
print(sum(jedynki))

import math
print(math.fsum(jedynki))

zbior = {(x, x**2, x**3) for x in range(-10,11)}
print(zbior)
print(len(zbior))

napisy = {'ala','ma','kota'}
slownik = {etk : len(etk) for etk in napisy}
print(slownik)