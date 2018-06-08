# poproś uzytkownika o decyzję czy iść w lewo czy w prawo

kierunek = input('Czy iść w lewo czy w prawo (l/p)? ')

if kierunek == 'l':
    print('idziemy w lewo')
    print('ala ma kota')
    print('jestem w gałęzi if')
elif kierunek == 'p':
    print('idziemy w prawo')
    print('kot ma alę')
    print('jestem w gałęzi elif')
else:
    print('nie rozumiem')
    print('jestem w gałęzi else')