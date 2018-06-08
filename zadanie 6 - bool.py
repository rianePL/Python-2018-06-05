# zadanie 6
liczba = float(input('Podaj liczbę do sprawdzenia : '))

print('Liczba jest wieksza niż 10:', liczba > 10)
print('Liczba mniejsza lub równa 15: ', liczba <= 15)
print('Liczba podzielna przez 2:', liczba % 2 == 0)

# zadanie 7
liczba = float(input('Podaj liczbę do sprawdzenia : '))

print(
      (liczba % 2 == 0) and (liczba % 3 == 0) and (liczba > 10)
      or liczba == 7
    )

# zadanie 8
szer = float(input('Podaj szerokość: '))
wys = float(input('Podaj wysokość: '))
dl = float(input('Podaj długość: '))

print('czy objętość większa niż 1 litr: ', szer * wys * dl > 1000)
