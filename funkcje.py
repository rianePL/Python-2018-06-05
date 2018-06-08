# funkcja - kawalek kodu, którego mogę wielokrotnie używać


def wypisz_powitanie():
    print('Witaj świecie!')

def zwróc_dwa():
    return 2

def dodaj(a, b):
    return a + b

def czy_pierwsza(liczba_do_sprawdzenia):
    # sprawdzam do pierwiastka ze sprawdzanej liczby
    for x in range(2,int(liczba_do_sprawdzenia ** (1/2))+1):
        if liczba_do_sprawdzenia % x == 0:
            return False
    return True


print('przed wykonaniem funkcji')
wypisz_powitanie()
wypisz_powitanie()
wypisz_powitanie()
print('po wywołaniu funkcji')

print(zwróc_dwa() + zwróc_dwa())
print(dodaj(2.6,5))
print(dodaj('ala','makota'))
# print(dodaj(5,'makota'))

print(czy_pierwsza(10))
print(czy_pierwsza(13))