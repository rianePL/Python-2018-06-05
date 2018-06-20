import sys
from collections import defaultdict

# lista argumentów wywołania programu
print(sys.argv)

wartosc_pocz = lambda : 1000
print(wartosc_pocz())
slownik = defaultdict(wartosc_pocz)
et = 'nowa'
slownik[et] +=1
slownik[et] +=1
slownik['ala'] +=1
print(slownik)

with open(sys.argv[1]) as plik_in:
    mails = defaultdict(int)
    for linia in plik_in:
        if linia.count('@') == 1:
            mails[linia.strip().lower().replace(' ','_')] += 1

dane = '\n'.join(f'{e} : {n}' for e,n in sorted(mails.items()))

with open(sys.argv[2], mode='w') as plik_out:
    # plik_out.writelines(x + '\n' for x in mails )
    plik_out.writelines(dane)