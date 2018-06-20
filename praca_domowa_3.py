# Zadanie 3
# Zaimplementuj funkcję zwracającą z przekazanego napisu
# zbiór słów o zadanej liczbie znaków. Wraz z implementacją
# funkcji dostarcz także zbiór testów.
#
# Przykład wywołania funkcji:
#
# >>> find_words('ala ma kota a kot ma ale', 3) {'ale', 'kot', 'ala'}
# >>> find_words('ala ma kota a kot ma ale', 10) set()

def find_words(zdanie, liczba_znaków=1):
    # wynik = set()
    # for wyraz in zdanie.split():
    #     if len(wyraz) == liczba_znaków:
    #         wynik.add(wyraz)
    # return wynik

    return {wyraz for wyraz in zdanie.split()
            if len(wyraz) == liczba_znaków}

def test_find_words_trzyliterowe():
    assert find_words('ala ma kota a kot ma ale', 3) == {'ale', 'kot', 'ala'}

def test_find_words_pusty():
    assert find_words('',3) == set()

def test_find_words_same_spacje():
    assert find_words('     ',1) == set()

def test_find_words_nie_ma_takiego_słowa():
    assert find_words('ala ma kota a kot ma ale', 10) == set()


def test_find_words_domyślny_argument():
    assert find_words('ala ma kota a kot ma ale') == {'a'}

def test_find_words_bez_spacji():
    assert find_words('alamakota',9) == {'alamakota'}

