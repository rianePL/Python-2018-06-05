# Zaimplementuj metode statyczna tworzaca koszyk na podstawie listy
# podanych produktów. Kazdy z nich powinien zostac dodany do
# koszyka tylko raz.
# Przykład uzycia:
# backset = Basket.with_products([prod_1, prod_2])


class Basket:

    def __init__(self):
        self.products = set()

    def __str__(self):
        return f'Basket: {self.products}'

    def add_product(self,prod):
        self.products.add(prod)

    @classmethod
    def with_products(cls, products_list):
        basket = cls()
        for p in products_list:
            basket.add_product(p)
        return basket


# przykład użycia
basket = Basket.with_products([('woda',10)
                                  ,('bułka',3.5)
                                  ,('pomarańcze',5)])
print(basket)