
produkcja = {'a','b','c','d'}
plik = {'a','b','e','f'}

# czego jeszcze nie ma w tabelach produkcyjnych:
plik - produkcja

# co już jest zaimportowane?
plik & produkcja

# czym się różnią?
plik ^ produkcja
(plik | produkcja) - (plik & produkcja)

# komplet danych
plik | produkcja


# Napisz program zliczajacy liczbe unikalnych liczb wprowadzonych
# przez uzytkownika. Sprawdz jak duzo z tych liczb jest liczbami
# parzystymi w zakresie 0-100 - w tym celu skorzystaj z operatora
# iloczynu.

zbior = set()
while True:
    liczba = input('podaj liczbę: ')
    if liczba == '':
        break
    zbior.add(float(liczba))

print('podałeś',len(zbior),'różnych wartości')

# parzyste = set()
# for a in range(0,101,2):
#     parzyste.add(a)

parzyste = set(range(0,101,2))

czesc_wspolna = zbior & parzyste
print('z tego', len(czesc_wspolna), 'parzystych 0-100')

print(zbior)
print(parzyste)
print(czesc_wspolna)