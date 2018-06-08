def formatuj(*args,**kwargs):

    # wynik = ''
    # for napis in args:
    #     wynik += napis + '\n'
    # wynik = wynik.rstrip('\n')

    # komu działa ten czyta z dokumentacji metode join

    wynik = '\n'.join(args)

    for podmien in kwargs:
        wynik = wynik.replace('$'+podmien, str(kwargs[podmien]) )

    return wynik


def test_pusty():
    assert formatuj('ala ma kota ') == 'ala ma kota '

def test_zcalanie():
    assert formatuj('ala', 'ma', 'kota') == 'ala\nma\nkota'

def test_zcalanie2():
    assert formatuj('ala', 'ma', 'ala') == 'ala\nma\nala'

def test_podmien():
    assert formatuj('ala ma $zwierzak', zwierzak='kota') == 'ala ma kota'

def test_docelowy():
    assert formatuj(
        'koszt $cena PLN',
        'kwota $cena brutto',
        cena=10,
    ) == 'koszt 10 PLN\nkwota 10 brutto'
