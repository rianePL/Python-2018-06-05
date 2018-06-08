# przed pętlą
# zapytaj użytkownika o a
# jeśli a nie jest liczbą to zakończ
# w przeciwnym przypadku a staje się pierwszym min i pierwszym max

# w pętli
# wejdź do pętli jeśli a jest liczbą
#   sprawdź czy a jest większa od najwiekszej
#       jeśli tak to podmień
#   analogicznie z minimum
#   zapytaj o następną liczbę (a)

# po pętli
# wypisz znalezione min i max


a = input('podaj liczbę lub [k] żeby skończyć: ')
if a == 'k':
    print('nie podałeś żadnej liczby!')
    exit()

liczba = float(a)
min = liczba
max = liczba

a = input('podaj liczbę lub [k] żeby skończyć: ')
while a !='k':
    liczba = float(a)
    if liczba < min:
        min = liczba
    if liczba > max:
        max = liczba
    a = input('podaj liczbę lub [k] żeby skończyć: ')

print(min, max)