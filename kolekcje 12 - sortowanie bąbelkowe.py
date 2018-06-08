# wybierz najmniejszy i ustaw na odpowiedniej pozycji

lista = [2,4,1,6,3,5,0]

# tak nie róbcie!!!
# przechodzenie po elementach listy,
# która jest modyfikowana wewnątrz pętli

# print(lista)
# for el in lista:
#     del lista[lista.index(el)]
#     print(lista)

# print(lista)
# for i in range(len(lista)):
#     del lista[i]
#     print(lista)

# lista2 = []
# lista2.append(minium_lokalne)

lista = [2,4,1,6,3,5,3,8,0]

for i in range(len(lista)):
    m_lok = min(lista[i:])
    poz = lista.index(m_lok,i)
    lista[poz] = lista[i]
    lista[i] = m_lok
    print(lista)

print('===========')
lista = [2,4,1,6,3,5,3,8,0]

for i in range(len(lista)):
    m_lok = min(lista[i:])
    poz = lista.index(m_lok,i)
    del lista[poz]
    lista.insert(i,m_lok)
    print(lista)

