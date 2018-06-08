x = int(input('podaj x: '))
if x < 0 or x > 100:
    print(f'niepoprawna pozycja x: {x}')
    exit(1)

y = int(input('podaj y: '))
if y < 0 or y > 100:
    print(f'niepoprawna pozycja y: {y}')
    exit(1)

marg_dolny = 10
rozmiar = 100
marg_górny = rozmiar - marg_dolny

if x <= marg_dolny:
    if y <= marg_dolny:
        print('lewy dolny róg')
    elif y >= marg_górny:
        print('lewy górny róg')
    else:
        print('lewa krawędź')

elif x >= marg_górny:
    if y <= marg_dolny:
        print('prawy dolny róg')
    elif y >= marg_górny:
        print('prawy górny róg')
    else:
        print('prawa krawędź')

else:
    if y <= marg_dolny:
        print('dolna krawędź')
    elif y >= marg_górny:
        print('górna krawędź')
    else:
        print('środek')

