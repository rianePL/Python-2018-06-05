plik = open('dane.txt',encoding='UTF-8')

zawartosc = plik.read(10)
print('pierwszy read:', zawartosc)

zawartosc = plik.read(10)
print('drugi read:',zawartosc)

plik.seek(0)
zawartosc = plik.read(10)
print('trzeci read:',zawartosc)

print('=======linia po linii =================')
plik.seek(0)
for nr, linia in enumerate(plik.readlines()):
    # print(nr, repr(linia))
    # print(nr, linia, end='')
    print(nr, linia.strip())

print('=======linia po linii jeszcze raz=======')
plik.seek(0)
for linia in plik:
    print(linia.strip())

plik.close()

# próba czytania z zamknietego pliku
# ValueError
# zawartosc = plik.read(10)

# nie ma takiego pliku
# FileNotFoundError
# plik = open('inny_plik.txt')

with open('dane.txt', mode='r', encoding='UTF-8') as plik_in:
    # blok kodu
    dane = plik_in.read()


with open('wyjscie.txt', mode='w', encoding='UTF-8') as plik_out:
    plik_out.write(dane + 'dodatkowa linia\n')
