# pusta lista
lista = []

while len(lista) < 10:
    lista.append(float(input('podaj liczbę: ')))

print(sum(lista)/len(lista))

# break przerywa działanie całej pętli
lista = []
a = input('podaj liczbę: ')
while a != '':
    lista.append(float(a))
    if len(lista) >= 10 :
        break
    a = input('podaj kolejną liczbę: ')
print('po pętli: ', lista)

# continue przerywa działanie tego jednego obrotu pętli
lista = []
for x in range(1,101):
    if x % 6 == 0:
        continue
    lista.append(x)
print('po pętli: ', lista)

