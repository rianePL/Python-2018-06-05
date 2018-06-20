import sys

nieskonczonosc = float('inf')
print(nieskonczonosc)

nieskonczonosc += 1000
print(nieskonczonosc)

if nieskonczonosc > 100000000:
    print('wieksze')
else:
    print('nie wieksze niz')

print(sys.float_info)

def fun_a(x):
    return -x

print(fun_a(-2))

zmienna = fun_a

print(zmienna(3))

lambda x : -x

fun_b = lambda x : x**2

print(fun_b(4))

porównaj = lambda x,y : x > y
moj_max = lambda x,y : x  if x>y else y

print(porównaj(3,4))

lista = [-1,2,-3,-9,-6,3,1,0,3]
print(max(lista))
print(max(lista, key=lambda x: x**2))

temp={'ala':2.5, 'ma':6, 'kota':1, 'szarego':1.5}
print(max(temp))    #max klucz
print(max(temp.values()))   #max wartosc
print(max(temp.keys())) # max klucz

# klucz dla max wartosci
print(max(temp, key=lambda x: temp[x]))

obs = [('data1', 3,7),('data2',5,15), ('data3',8,13)]
# data dla maksymalnej amplitudy
print(max(obs, key= lambda tupla: tupla[2]-tupla[1])[0] )