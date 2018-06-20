slownik = {'ala':5, 'ola':7, 'ula':0}
lista = [1,2,3,4,5,6,7]

try:
    print('przed błędem')
    imie = 'ula'
    a = 1/slownik[imie]
    b = lista[6]
    'ala' + 3
    print('po błędzie')

except ZeroDivisionError:
    # obsłuż ile umiesz
    print('w bloku obsługi błędu dzielenia przez 0')
    # i rzuć wyjątek wyżej
    raise

except KeyError as wyjatek:
    print('nie ma takiego wpisu w słowniku')
    print(wyjatek.args)

except IndexError:
    print('poza listą')
except TypeError:
    print('niepoprawna operacja na typach')
except NameError:
    print('nieznana nazwa')

finally:
    print('sprzatanie, zawsze się wykona')
# except :
#     print('inne wyjątki')

print('po bloku try')

a = float(input('podaj liczbę'))