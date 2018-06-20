# definicja klasy (foremka)
class Samochod:
    # metody
    def __init__(self, nazwa, pojemność):
        self.pojemność = pojemność
        self.nazwa = nazwa

    def przedstaw_sie(self):
        print('Nazywam się:',self.nazwa,'. Jestem samochodem')
# CamelCase

# obiekty (ciastka)
mały_fiat = Samochod('maluch',.6)
alfa = Samochod('piekna i bestia',3.0)
ferrari = Samochod('strzała',6.0)

print(mały_fiat)
print(alfa)
print(ferrari)

mały_fiat.przedstaw_sie()
alfa.przedstaw_sie()
ferrari.przedstaw_sie()