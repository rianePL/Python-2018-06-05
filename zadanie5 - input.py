# przelicza koszt podróży pomiędzy dwoma punktami

miasto_a = input('Miasto A : ')
miasto_b = input('Miasto B : ')

dystans_str = input(f'Odleglość pomiędzy miastami {miasto_a}-{miasto_b} : ')
dystans = float(dystans_str)

cena_paliwa = float(input('Cena paliwa : '))
spalanie = float(input('Spalanie na 100 km : '))

koszt_podrozy = dystans / 100 * spalanie * cena_paliwa

print(f'Całkowity koszt podróży to {koszt_podrozy:.2f} PLN')
# print('całkowity koszt',round(koszt_podrozy,2),'pln')