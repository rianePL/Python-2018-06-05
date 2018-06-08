# zadanie: wypisz tabliczkę mnożenia 10x10

#  1  2  3  4  5 ... 10
#  2  4  6  8 10 ... 20
# ...
# 10 20 30 40 50... 100

print('tabliczka mnożenia za pomocą while:')
x = 1
while x <= 10:
    y = 1
    while y <= 10:
        print(f'{x*y:5}', end=' ')
        y+=1
    print()
    x+=1

print('to samo za pomocą for:')

print(' '*3, end='   ')
for x in range(10):
    print(f'{x:3}', end=' ')
print()
print()
for x in range(10):
    print(f'{x:3}', end='   ')
    for y in range(10):
        print(f'{x*y:3}', end=' ')
    print()