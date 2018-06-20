import json

dane = {'user': 'user-1', 'action': 'LOGIN', 'time': 45}

# zapisz dane w postaci json
dane_json = json.dumps(dane)

print(repr(dane))
print(repr(dane_json))

# odczytaj dane w postaci json
dane_pobrane = json.loads(dane_json)
print(dane_pobrane)

# pobieranie danych z pliku
with open('dane.json', encoding='UTF-8') as plik:
    dane_pobrane = json.load(plik)

print(dane_pobrane)

dane_pobrane.append({'prod':'rzodkiewka', 'cena':4.7, 'ilosc':2})
print(dane_pobrane)

# zapisywanie danych do pliku
with open('raport.json', mode='w', encoding='UTF-8') as plik:
    json.dump(dane_pobrane, plik)

with open('raport.json') as plik:
    print(json.load(plik))