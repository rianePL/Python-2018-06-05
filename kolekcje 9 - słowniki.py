# wypisz listę towarów
# poproś o towar
# poproś o ilość
# wypisz koszt

towary = {'jabłko':4.5, 'gruszka':6.5, 'ziemniaki':3, 'marchew':2.1}

# list(słownik.keys())
# słownik['ola']
# 'ola' in słownik
print('Oferta: ', towary)
koszt = 0

while True:
    wybrany_towar = input('wybierz towar: ')

    if wybrany_towar == '':
        break

    if wybrany_towar not in towary:
        print('nie ma takiego towaru!')
        continue

    cena = towary[wybrany_towar]
    print(wybrany_towar, ' kosztuje ', cena, ' pln za kg')

    ilość = float(input('ile chcesz kupić? '))
    koszt += cena * ilość
    print('suma pozycji: ', cena * ilość)
    print('suma koszyka: ', koszt)

print('ostateczny koszt to ', koszt , ' pln')