# policz ile razy wystąpiły poszczególne litery w zadanym napisie

zliczacz = {}
zliczacz = dict()

print(zliczacz)

napis = 'ala ma kota'
# wynik = {'a':4,'l':1,' ':2,'m':1,'k':1,'o':1,'t':1}

for znak in napis:
    print(znak)
    if znak in zliczacz.keys():
        zliczacz[znak] += 1
    else:
        zliczacz[znak] = 1
    print(zliczacz)