class Produkt:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def print_info(self):
        return f'{self.name} ({self.id}), cena: {self.price:.2f}'

    def value(self, amount):
        return amount * self.cena


class Basket():
    def __init__(self):
        self.products = {}


    def generate_report(self):
        wynik = 'Produkty w koszyku:\n'
        if not self.products:
            wynik += 'brak\n'
        for prod in self.products:
            wynik += f'{prod.print_info()} x {self.products[prod]}\n'
        wynik += f'W sumie: {self.count_total_price():.2f}'
        return wynik

    def add_product(self, product, amount):
        if product not in self.products:
            self.products[product] = amount
        else:
            self.products[product] += amount

    def count_total_price(self):
        total = 0
        for pr in self.products:
            total += pr.value(self.products[pr])
        return total

def test_Basket_new():
    basket = Basket()
    assert basket.generate_report() == 'Produkty w koszyku:\nbrak\nW sumie: 0.00'

def test_Basket_final():
    basket = Basket()

    prod = Produkt(1,'woda',10)
    basket.add_product(prod,3)

    prod = Produkt(2,'cola',3)
    basket.add_product(prod,5)
    basket.add_product(prod,8)

    assert basket.count_total_price() == 69
    print(basket.generate_report())
