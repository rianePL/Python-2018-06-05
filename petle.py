a = 1
while a < 10:
    print(a)
    a = a + 1

print('koniec')

# kwadraty wszystkich liczb
a = 1
while a <= 100:
    print(a ** 2)
    a += 1  # a = a + 1

print('koniec kwadratów')

# kwadraty parzystych
print('kwadraty parzystych:')

a = 2
while a <= 100:
    print(a ** 2)
    a += 2

print('koniec kwadratów liczb parzystych')

# kwadraty nieparzystych
print('kwadraty nieparzystych:')

a = 1
while a <= 100:
    print(a ** 2)
    a += 2

print('koniec kwadratów liczb nieparzystych')

# suma kwadratów liczby nieparzystych
print('suma kwadratów liczby nieparzystych:')
suma = 0
a = 1
while a < 10:
    suma += a ** 2
    print(suma)
    a += 2

print('koniec')

# pętla FOR
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for a in lista:
    print(a ** 2)

# policz ujemne i dodatnie liczby na liście
lista = [-2, 0, 3, -4, -6, 0, 9, 23, 1]
dodatnie = 0
ujemne = 0
for a in lista:
    if a > 0:
        dodatnie += 1
    elif a < 0:
        ujemne += 1
print('dodatnie:',dodatnie, ', ujemne:',ujemne)

# wypisz liczby od 0 do 9
for x in range(10):
    print(x)

# wypisz liczby od 1 do 10
for x in range(1, 11):
    print(x)

# wypisz liczby od 1 do 10 z krokiem 3
for x in range(1, 11, 3):
    print(x)

# wypisz wszystkie liczby podzielne przez 3 lub 5
licznik = 0
for liczba in range(101):
    if liczba % 3 == 0 or liczba % 5 == 0:
        print(liczba)
        licznik += 1
print(f'znalazłam {licznik} liczb podzielnych przez 3 lub 5')