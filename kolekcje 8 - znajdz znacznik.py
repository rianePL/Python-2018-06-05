# policz długość znacznika pomiedzy znakami < >
napis = 'Ala ma <kota> a kot ma Alę'

pozycja_otw = napis.find('<')
pozycja_zamk = napis.find('>')

print(pozycja_otw, pozycja_zamk)
print('długość znacznika : ',pozycja_zamk - pozycja_otw - 1 )

# zadanie z *
# a co jeśli znaczników jest więcej?
napis = 'Ala ma <kota>, a <kot> ma Alę'

otw = []
zamk = []
for x in range(len(napis)):
    if napis[x] == '<':
        otw.append(x)
    if napis[x] == '>':
        zamk.append(x)

licznik=0
for x in range(len(otw)):
    licznik += zamk[x] - otw[x] -1

print('suma dł znaczników: ', licznik)

# zadanie z **
# a co jeśli znaczniki się zagnieżdżają?
# 'ala <ma <kota> ładnego>'
# wynik : 19 ('kota' * 2)

napis = 'ala <ma <kota> ładnego>'
licznik = 0
poziom = 0

for a in napis:
    if a == '<':
        poziom += 1
    elif a == '>':
        poziom -= 1
    else:
        licznik += poziom
print('sumaryczna dł zagnieżdżonych: ',licznik)

