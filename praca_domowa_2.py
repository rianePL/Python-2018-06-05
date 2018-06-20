# Zadanie 2
# Zaimplementuj program znajdujący największą oraz najmniejszą
# amplitudę temperatury wśród temperatur wprowadzonych przez
# użytkownika. Poproś użytkownika także o podanie daty pomiaru
# temperatury.
#
# Wykorzystaj jedną listę do przechowywania wszystkich danych
# wprowadzonych przez użytkownika w celu ich późniejszego
# wypisania. Elementami listy powinny być trzyelementowe
# tuple (data, minimalna temperatura, maksymalna temperatura).
# Zakończenie pobierania powinno być możliwe dzięki komendzie
# KONIEC.
#
# Przykład działania programu:
#
# Podaj datę lub wpisz KONIEC: 01.01.2017
# Minimalna temperatura dnia 01.01.2017: -2.5
# Maksymalna temperatura dnia 01.01.2017: 1.4
# Podaj datę lub wpisz KONIEC: 02.01.2017
# Minimalna temperatura dnia 02.01.2017: -6.1
# Maksymalna temperatura dnia 02.01.2017: 0.4
# Podaj datę lub wpisz KONIEC: 03.01.2017
# Minimalna temperatura dnia 03.01.2017: -9.0
# Maksymalna temperatura dnia 03.01.2017: 4.4
# Podaj datę lub wpisz KONIEC: KONIEC
# Zebrano 3 pomiary temperatur:
# - data: 01.01.2017, min: -2.5, max: 1.4 - minimalna amplituda
# - data: 02.01.2017, min: -6.1, max: 0.4
# - data: 03.01.2017, min: -9.0, max: 4.4 - maksymalna amplituda

obserwacje = []
while True:
    data = input('Podaj datę lub wpisz KONIEC:')
    if data == 'KONIEC':
        break

    min_t = float(input(f'Minimalna temperatura dnia {data}:'))
    max_t = float(input(f'Maksymalna temperatura dnia {data}:'))

    if min_t > max_t:
        print('lama')
        continue

    tupla = (data, min_t, max_t)
    obserwacje.append(tupla)

if len(obserwacje) == 0:
    exit('Brak danych')

min_ampl = obserwacje[0][2]-obserwacje[0][1]
max_ampl = min_ampl
for pomiar in obserwacje:
    ampl = pomiar[2] - pomiar[1]
    if ampl < min_ampl:
        min_ampl = ampl
    elif ampl > max_ampl:
        max_ampl = ampl

print(f'Zebrano {len(obserwacje)} pomiary temperatur:')
for pomiar in obserwacje:
    znacznik = ''
    if pomiar[2] - pomiar[1] == max_ampl:
        znacznik = ' - maksymalna amplituda'
    elif pomiar[2] - pomiar[1] == min_ampl:
        znacznik = ' - minimalna amplituda'
    print(f'data: {pomiar[0]}, min: {pomiar[1]}, '
          f'max: {pomiar[2]} ', znacznik)

    # a=0 ? 1 : 2   <== tak się pisze w innych językach
    # 1 if a==0 else 2  <== tak się pisze w pythonie
