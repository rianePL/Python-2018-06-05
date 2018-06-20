# Zadanie 1
# Wiedząc, że kurs EUR to 4,20, kurs USD to 3.54,
# natomiast kurs CHF to 3,58 przygotuj program,
# który pozwoli użytkownikowi policzyć koszt zakupu
# lub sprzedaży poszczególnych walut.
# Wykonując program załóż, że kwota sprzedaży
# i kupna jest taka sama.
#
# Przykład działania programu:
#
# Czy chcesz dokonać kupna, czy sprzedaży? [k/s] k
# Jaką walutę chcesz zakupić? [EUR/USD/CHF] EUR
# Ile złotówek chcesz wymienić? 100
# Możesz zakupić 23,80 EUR
#
import math

kursy = {'EUR':4.20, 'USD':3.54, 'CHF':3.58}
print(kursy)

operacja = input('Czy chcesz dokonać kupna, czy sprzedaży? [k/s]').lower()
if operacja == 'k':
    # waluta = input(f'Jaką walutę chcesz zakupić? {[*kursy.keys()]}')
    waluta = input(f'Jaką walutę chcesz zakupić? '
                   f'[{"/".join(kursy.keys())}]').upper()
    if waluta not in kursy:
        exit(f'niepoprawna waluta {waluta}')

    ile = float(input('Ile złotówek chcesz wymienić?'))
    print('Możesz zakupić ', math.floor(ile / kursy[waluta] * 100) / 100, waluta)
    print(f'Możesz zakupić {math.floor(ile / kursy[waluta] * 100) / 100:.2f}', waluta)

elif operacja == 's':
    waluta = input(f'Jaką walutę chcesz sprzedać? '
                   f'[{"/".join(kursy.keys())}]').upper()
    if waluta not in kursy:
        exit(f'niepoprawna waluta {waluta}')

    ile = float(input('Ile waluty chcesz wymienić?'))
    print(f'Dostaniesz {math.floor(ile * kursy[waluta] * 100) / 100:.2f} PLN')
else:
    print('niepoprawna operacja: ',operacja)