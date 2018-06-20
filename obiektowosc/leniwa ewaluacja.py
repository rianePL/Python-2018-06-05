# Python jest leniwy i dobrze nam z tym!
def wypisz():
    print('jestem')
    return True


if 1!=1 or wypisz():
    print('udało się')

# puste obiekty wyliczają sie do False
# jeśli obiekt ma jakieś elementy to wylicza się do True
status = ''
b='ala ma kota'
print (status or b)

status = 'coś'
b='ala ma kota'
print (status or b)

lista = []
if lista:
    print('w liście są elementy')
else:
    print('lista jest pusta')

str1, str2, str3 = '','ala','makota'
pierwszy_niepusty = str1 or str2 or str3
print(pierwszy_niepusty)