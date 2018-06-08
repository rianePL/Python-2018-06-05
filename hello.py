print('Hello World!')

imie = 'Agata'
wzrost = 170

komunikat1 = 'Imię : ' + imie + '\n Wzrost : ' + str(wzrost)
print(komunikat1)
komunikat2 = f'Imię : {imie} \n Wzrost : {wzrost}'
print(komunikat2)
print('Imię :', imie, '\n Wzrost :', wzrost)

cena_za_kg = 10.
waga = 2.5
print(f'''
Cena za kg : {cena_za_kg}
Waga : {waga}
Należność : {cena_za_kg * waga}
''')

cena_str = input('podaj cenę jabłek : ')
cena_float = float(cena_str)

waga_str = input('podaj wagę jabłek: ')
cena = float(input('podaj cenę jabłek : '))
print('wpisałeś : ', cena, waga)
print('należność: ', float(cena) * float(waga))
