# jak sprawdzić czy napis jest liczbą (całkowitą)
#
# if 'ala ma kota'.isdecimal():
#     print('to jest liczba')
# else:
#     print('to nie jest liczba')
#
# if '12345'.isdecimal():
#     print('to jest liczba')
# else:
#     print('to nie jest liczba')

# przed pętlą
# licznik na -1
# suma na 0
# ustaw pierwszą liczbę na '0'

# pętla
# dopóki wczytujesz liczby
#   zamień na liczbę
#   zwiększ sumę
#   zwiększ licznik
#   zapytaj o koleną liczbę

# po pętli (już nie ma kolejnej liczby)
# sprawdź czy licznik nie jest 0
# wylicz średnią

licznik = -1
suma = 0
liczba = '0'

while liczba.isdecimal():
    licznik += 1
    suma += int(liczba)
    liczba = input('podaj kolejną temp: ')

if licznik == 0:
    print('Brak danych')
    exit(0)

srednia = suma / licznik
print(f'średnia podanych temp: {srednia}')
