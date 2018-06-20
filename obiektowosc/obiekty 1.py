# Zaimplementuj klase Product przechowujaca informacje o cenie,
# nazwie oraz ID produktu. Zaimplementuj metode wypisujaca
# informacje o produkcie na konsole.
# Przykład uzycia:
# >>> product = Product(1, 'Woda', 10.99)
# >>> product.print_info()
# Produkt "Woda", id: 1, cena: 10.99 PLN

class Produkt:
    def __init__(self,id, nazwa, cena):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena

    def print_info(self):
        print(f'Produkt "{self.nazwa}", id: {self.id}, cena: {self.cena} PLN')


produkt1 = Produkt(1,'Woda',10.99)
produkt1.print_info()
