def splaszcz(lista):
    # warunek stopu
    if len(lista) == 0:
        return lista

    # wywołanie rekurencyjne
    for i, el in enumerate(lista):
        if type(el) == type([]):
            lista[i:i+1] = splaszcz(el)

    # zwrócenie wyniku
    return lista


def test_pusta():
    assert splaszcz([]) == []

def test_pusta2():
    assert splaszcz([[]]) == []

def test_jeden_el():
    assert splaszcz([4]) == [4]

def test_plaska():
    assert splaszcz([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_zagniezdzenie():
    assert splaszcz([1, [2, 3], 4, 5]) == [1, 2, 3, 4, 5]

def test_zagniezdzenie2():
    assert splaszcz([1, [2], 3, [4]]) == [1, 2, 3, 4]

def test_zagniezdzenie3():
    assert splaszcz([1, [[2], 3, 4]]) == [1, 2, 3, 4]
