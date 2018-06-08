# Tupla == krotka
# dwójka, trójka, czwórka elementów

#tuple są niemodyfikowalne
tupla = (1,2,3)
tupla2 = tupla

krotka = (1, 'ala', 4.5, 'ma kota')
krotka = (1,(1,2,3),'ala')
krotka = ('ala','ola','ela','ula','aga','oda','gaga')
jednoelementowa = ('a',)

print(tupla)
print(tupla2)
print(krotka)
print(jednoelementowa)

# elementy krotki numerujemy od 0
print(krotka[2])
print(krotka[-1])
# print(krotka[3])

print(krotka[1:-1])
print(krotka[3:])
print(krotka[:5])
print(krotka[:])

print(id(krotka))
print(id(krotka[:]))

print(krotka[1::2])
print(krotka[::-2])

print(len(krotka))

if 'ola' in krotka:
    print('znaleziona')
else:
    print('nie ma w kolekcji')


# Listy
# są modyfikowalne

lista = [1,2,3,4,5]
lista = [1, 3.4, 'ala ma kota',(1,2,3),['a','m','i']]

print(lista)
print(lista[1:4])
print(lista[::-1])
print(len(lista))
print(len(lista[3]))
print(lista[3][0])
print(type(lista[3]))

lista[2] = 5
print(lista)

lista[:3] = [6,6,6,6,6,6,6]
print(lista)

lista.append('nowy element')
print(lista)

lista.insert(4,'wstawiony')
print(lista)

del lista[5:8]
print(lista)

print(id(lista))
print(id(lista[:]))

# krotki nie mogę modyfikować
# krotka[1] = 'ala ma kota'
