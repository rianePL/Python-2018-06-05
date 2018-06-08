# znajdz najwiekszy i najmniejszy element
# i zamien je miejscami

lista = [2, 90, 4, -2, 17, -200, -3, 30, 1]

# dwa sposoby chodzenia po listach:
#1
for i,x in enumerate(lista):
    print(i,x)
#2
for i in range(len(lista)):
    print(i, lista[i])

# sposób na sprawdzenie czy wartość 90 jest na liscie
# a jeśli tak to na której pozycji
max = 90
if max in lista:
    poz_max = lista.index(max)
print(poz_max)

if lista == []:
    exit()

# metoda tradycyjna
poz_min = 0
poz_max = 0
for i in range(len(lista)):
    if lista[i] < lista[poz_min]:
        poz_min = i
    if lista[i] > lista[poz_max]:
        poz_max = i

tmp = lista[poz_max]
lista[poz_max] = lista[poz_min]
lista[poz_min] = tmp

# ze wsparciem mechanizmów pythona
print(lista)

poz_min = lista.index(min(lista))
poz_max = lista.index(max(lista))
lista[poz_min], lista[poz_max] = lista[poz_max], lista[poz_min]

print(lista)