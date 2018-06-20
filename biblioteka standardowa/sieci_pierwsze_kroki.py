# wczytaj dane z nbp
# stwórz słownik kursów walut
# spytaj użytkownika ile złotówek chce wymienić
# i na jaką walutę
# przelicz ile waluty może kupić

import urllib.request
import json

# with urllib.request.urlopen('http://pywaw.org') as response:
#     print(response.read().decode('utf-8'))

with urllib.request.urlopen('http://api.nbp.pl/api/exchangerates/tables/a/?format=json') as response:
    dane_surowe = response.read().decode('utf-8')

dane_przetworzone = json.loads(dane_surowe)
print(dane_przetworzone[0]['rates'])

# 1
kursy = {}
for i in dane_przetworzone[0]['rates']:
    kursy[i['code']] = i['mid']

# 2
kursy = {i['code']:i['mid'] for i in dane_przetworzone[0]['rates']}

while True:
    akcja = input('''Co chcesz zrobić?
        [k]upic walutę
        [s]przedać walutę
        [w]ypisać kursy 
        [ENTER] zakończyć: ''')

    if akcja == '':
        break

    if akcja == 'k':
        waluta = input('podaj kod waluty: ').upper()
        if waluta not in kursy:
            print('nie ma takiej waluty')
            continue
        ile = float(input('ile PLN chcesz wymienić? '))
        print(f'możesz kupić {ile/kursy[waluta]:.2f} {waluta}')


