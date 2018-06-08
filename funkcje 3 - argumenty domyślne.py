# Napisz funkcje obliczajaca liczbe znaków w zadanym napisie
# pomiedzy zadanymi znakami. Znaki, pomiedzy którymi ma odbywac
# sie zliczanie, powinny byc argumentami z wartosciami domyslnymi -
# odpowiednio < i >. Nawiasy moge byc zagniezdzone i moga
# wystapic wiele razy. Znaki pomiedzy zagniezdzonymi nawiasami
# liczone sa zgodnie z poziomem zagniezdzenia.
# Przykład uzycia:
# >>> policz_znaki('ala ma <kota> a kot ma ale')
# 4
# >>> policz_znaki('ala [kota [a kot]] ma [ale]', '[', ']')
# 18
# >>> policz_znaki('a <a<a<a>>>')
# 6

def policz_znaki(napis, naw_otw='<', naw_zam='>'):
    licznik = 0
    poziom = 0

    for a in napis:
        if a == naw_otw:
            poziom += 1
        elif a == naw_zam:
            poziom -= 1
        else:
            licznik += poziom

    return licznik


def test_pusty():
    assert policz_znaki('') == 0

def test_bez_nawiasow():
    assert policz_znaki('ala ma kota') == 0

def test_pojedynczy():
    assert policz_znaki('ala ma <kota> a kot ma ale') == 4

def test_pojedynczy2():
    assert policz_znaki('ala ma <koteczka> a kot ma ale') == 8

def test_zagniezdzenie():
    assert policz_znaki('a <a<a<a>>>') == 6

def test_argumenty():
    assert policz_znaki('ala [kota [a kot]] ma [ale]', '[', ']') == 18