# policz ile jest samogłosek w podanym przez użytkownika napisie

napis = 'ala ma kota, a kot ma alĘ'

# podpowiedzi
# if 'a' in napis:
#     print('w napisie wystepuje litera "a"')
#
# print('litera na 4 pozycji to: ',napis[4])
# print('długość napisu: ', len(napis))

licznik = 0
for s in napis.lower():
    if s in 'aeiouyąęó':
        licznik += 1
print('w napisie "', napis, '" jest ', licznik, ' samogłosek')

# ile razy występuje 'a' w napisie 'ala ma kota'
# 'ala ma kota'.count('a')

licznik = 0
kopia = napis.lower()
for s in 'aeiouyąęó':
    licznik += kopia.count(s)
print('w napisie "', napis, '" jest ', licznik, ' samogłosek')
