# zmienne prywatne zaczynamy od _

# 3 pliki:
# a) klasa
# b) testy
# c) użycie

class CashMachine:
    def __init__(self):
        self._banknotes = dict.fromkeys([200, 100, 50, 20], 0)

    def info(self):
        return 'jestem bankomat'

    def put_money(self, banknotes):
        for nom in self._banknotes:
            self._banknotes[nom] += banknotes.count(nom)

    def is_available(self):
        return sum(self._banknotes.values()) > 0

    def withdraw_money(self, amount):
        # b = sorted(dict.keys(), reverse=True)
        # dzielenie / // %
        # dla każdego nominału:  amount // nom
        # min wynik dzielenia i ile mamy
        #
        # alternatywnie pojedyncze banknoty przepisujemy do listy
        #
        # kwota jest zgodna => konczymy, sukces
        # nie ma nominałów mniejszych niż żądana kwota => kończymy, porażka
        b_reserved = dict.fromkeys(self._banknotes.keys(), 0)
        for nom in sorted(self._banknotes.keys(), reverse=True):
            b_no = min(amount // nom, self._banknotes[nom])
            # algorytm jest trudniejszy niż nam się wydawało :(
            if b_no > 0 \
                    and 0 < (amount - (b_no * nom)) < 50 \
                    and (amount % (b_no * nom)) % 20 != 0:
                b_no -= 1
            b_reserved[nom] = b_no
            amount -= b_no * nom
        if amount == 0:
            for nom in self._banknotes:
                self._banknotes[nom] -= b_reserved[nom]
            return self._dict_to_list(b_reserved)
        else:
            return []

    def _dict_to_list(self, banknotes):
        ret = []
        for nom in banknotes:
            ret.extend([nom] * banknotes[nom])
        return ret


def test_CashMachine_empty():
    cash_machine = CashMachine()
    assert not cash_machine.is_available()


def test_CashMachine_load():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.is_available()


def test_CachMachine_withdraw():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.withdraw_money(150) == [100, 50]


def test_CachMachine_withdraw_20():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50, 20, 20, 20, 20])
    assert cash_machine.withdraw_money(80) == [20, 20, 20, 20]


def test_CachMachine_withdraw_210():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 50, 50, 20, 20, 20, 20])
    assert cash_machine.withdraw_money(210) == [100, 50, 20, 20, 20]


def test_CachMachine_withdraw_fail():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.withdraw_money(500) == []
