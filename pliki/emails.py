# wczytać plik z adresami email
# wyczyścić
#     usunąć nadmiarowe spacje
#     zmienić wielkość liter na małe
#     usunąć nieprawidlowe adresy
#         prawidlowy adres ma dokladnie 1 @
# zapisać do nowego pliku
#     każdy adres email tylko raz

with open('emails.txt') as plik_in:
    mails = set()
    for linia in plik_in:
        if linia.count('@') == 1:
            mails.add(linia.strip().lower().replace(' ','_'))

dane = '\n'.join(sorted(mails))

with open('emails_cleaned.txt', mode='w') as plik_out:
    # plik_out.writelines(x + '\n' for x in mails )
    plik_out.writelines(dane)