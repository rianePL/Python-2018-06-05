liczba1 = float(input('podaj pierwszą liczbę: '))
liczba2 = float(input('podaj drugą liczbę: '))

operacja = input('co wykonać? (+ - * /) ')

if operacja == '+' :
    print(f'wynik dodawania {liczba1} + {liczba2} = {liczba1+liczba2}')

elif operacja == '-':
    print(f'wynik odejmowania {liczba1} - {liczba2} = {liczba1-liczba2}')

elif operacja == '*':
    print(f'wynik mnożenia {liczba1} * {liczba2} = {liczba1*liczba2}')

elif operacja == '/':
    if liczba2 == 0:
        print('nie mogę podzielić przez 0!')
    else:
        print(f'wynik dzielenia {liczba1} / {liczba2} = {liczba1/liczba2}')

else:
    print(f'niepoprawna operacja: {operacja}')