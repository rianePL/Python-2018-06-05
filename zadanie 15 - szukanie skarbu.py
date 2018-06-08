# plansza 10x10
# losowa pozycja gracza
# losowa pozycja skarbu
# liczymy kroki
# podpowiadamy 'ciepło' / 'zimno'
import random

# przed pętlą
#   wylosować pozycję gracza
#   wylosować pozycję skarbu
#   licznik ruchów na 0

gracz_x = random.randint(1, 10)
gracz_y = random.randint(1, 10)

skarb_x = random.randint(1, 10)
skarb_y = random.randint(1, 10)

licznik = 0
odleglosc = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)
max_licznik = odleglosc+6

print('gracz:', gracz_x, gracz_y)
print('skarb:', skarb_x, skarb_y)

# w pętli
# wychodzimy z pętli jeśli znaleźliśmy skarb
#   lub wyszliśmy poza planszę
# warunek wejścia do pętli:
#   jesteśmy na planszy, ale nie na pozycji skarbu
#
while ((gracz_x != skarb_x or gracz_y != skarb_y)
       and 1 <= gracz_x <= 10
       and 1 <= gracz_y <= 10):

    if licznik == max_licznik:
        print('przekroczyłeś limit, smok się wyniósł')
        skarb_x = random.randint(1, 10)
        skarb_y = random.randint(1, 10)
        odleglosc = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)
        max_licznik += odleglosc + 6
        print('gracz:', gracz_x, gracz_y)
        print('skarb:', skarb_x, skarb_y)

    #   pytamy o nowy ruch
    ruch = input('w którą stronę idziesz? [l,p,g,d] ')

    #   zwiększamy licznik ruchów
    licznik += 1

    #   zmieniamy pozycję gracza zgodnie z ruchem
    #   podpowiadamy 'ciepło/zimno'
    if ruch == 'l':
        gracz_x -= 1
    elif ruch == 'p':
        gracz_x += 1
    elif ruch == 'd':
        gracz_y -= 1
    elif ruch == 'g':
        gracz_y += 1
    else:
        print('nie ma takiego kierunku :P')

    odleglosc2 = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)
    if random.randint(1,1000) <= 800 :
        if odleglosc > odleglosc2:
            print('ciepło')
        else:
            print('zimno')
    else:
        print('nie powiem')
    odleglosc = odleglosc2

    # debug
    print('gracz:', gracz_x,gracz_y)
    print('skarb:', skarb_x, skarb_y)


# po pętli
# albo spadłeś (hahaha)
# albo gratulacje + ile ruchów
print(f'wykonałeś {licznik} ruchów i....')
if gracz_x == skarb_x and gracz_y == skarb_y:
    print('ZNALAZŁEŚ SKARB!!!')
else:
    print('spadłeś! hahahaah')

