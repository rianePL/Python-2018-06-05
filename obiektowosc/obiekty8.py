from obiektowosc import obiekty5

class PrzepełnionaSzuflada(Exception):
    pass

class BrakPieniędzy(Exception):
    pass

class CashMachineLimits(obiekty5.CashMachine):

    def __init__(self, cap):
        super().__init__()
        self._cap = cap

    def put_money(self, banknotes):
        super().put_money(banknotes)
        if max(self._banknotes.values()) > self._cap:
            raise PrzepełnionaSzuflada

    def withdraw_money(self, amount):
        ret = super().withdraw_money(amount)
        if ret == []:
            raise BrakPieniędzy
        return ret

bank = CashMachineLimits(3)
try:
    bank.put_money([100,50,100,200,20,20,20])
    wallet = bank.withdraw_money(230)
    print(wallet)
except PrzepełnionaSzuflada:
    print('za dużo banknotów')
except BrakPieniędzy:
    print('Tej kwoty nie da się zrealizować')