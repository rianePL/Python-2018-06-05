# co wie o sobie pracownik:
# imie, nazwisko, pensja, rok urodzenia

# w pętli
#   wczytaj pracownika z konsoli

# na koniec zapisz wszystkich pracowników w pliku json
import json

class Employee:
    def __init__(self, fname, lname, sal, birth_y):
        self.fname = fname
        self.lname = lname
        self.sal = sal
        self.birth_y = birth_y

    def __str__(self):
        return f'{self.fname} {self.lname}: {self.sal}PLN, {self.birth_y}r'

    def to_dict(self):
        return {'fname':self.fname,
                'lname':self.lname,
                'sal':self.sal,
                'birth_y':self.birth_y}

    @classmethod
    def from_dict(cls,dict):
        return cls(dict['fname']
                   ,dict['lname']
                   ,dict['sal']
                   ,dict['birth_y'])

FILE_NAME = 'baza.json'

try:
    with open(FILE_NAME) as plik:
        lista_s = json.load(plik)

    lista_plac = [Employee.from_dict(dict) for dict in lista_s]
except:
    lista_plac = []

# wczytaj pracowników (z konsoli)

while True:
    action = input('''co chcesz zrobić: 
    [d]odaj pracownika 
    [u]sun pracownika
    [w]ypisz listę pracowników
    [k]oniec pracy?: ''')

    if action == 'k':
        break

    if action == 'w':
        print('====Lista pracowników:===')
        for i, prac in enumerate(lista_plac, start=1):
            print(f'[{i}] {prac}')
        print('=========================')
        continue

    if action == 'd':
        fname = input('podaj imie: ')
        lname = input('podaj nazwisko: ')
        sal = input('podaj pensję: ')
        birth_y = input('podaj rok urodzenia: ')

        prac = Employee(fname,lname,sal,birth_y)
        lista_plac.append(prac)
        continue

    if action == 'u':
        no = int(input('podaj numer pracownika do usunięcia: '))
        del lista_plac[no-1]
        continue

lista_s = [prac.to_dict() for prac in lista_plac]

# print(lista_plac)
# print(lista_s)
with open(FILE_NAME, mode='w') as plik:
    json.dump(lista_s, plik)
