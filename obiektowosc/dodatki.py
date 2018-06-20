class Faktura:

    def __init__(self, nabywca, sprzedawca, kwota):
        self.nabywca = nabywca
        self.sprzedawca = sprzedawca
        self.kwota = kwota

    def __str__(self):
        return f'od {self.sprzedawca}, ' \
               f'dla {self.nabywca}, ' \
               f'kwota={self.kwota}'

    @classmethod
    def faktura_dla_kowaskiego(cls,sprzedawca, kwota):
        return cls('Kowalski', sprzedawca, kwota)

#     użycie
faktura_zwykła = Faktura('Ewa', 'Jan', 300)
faktura_2 = Faktura.faktura_dla_kowaskiego('Rysiek',5000)

print(faktura_zwykła)
print(faktura_2)