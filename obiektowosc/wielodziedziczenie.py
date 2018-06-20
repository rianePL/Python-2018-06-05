class A:

    def __init__(self):
        self.ala = 5
        print('jestem w init A')

    def __str__(self):
        return 'jestem A'

    def kopnij(self):
        return 'goooool'


class B:
    def __init__(self):
        self.ala = 6
        self.bela = 7
        print('jestem w init B')

    def __str__(self):
        return 'jestem B'

    def trenuj(self):
        return 'biegaj szybciej! no już!'


class C(A,B):
    def __init__(self):
        B.__init__(self)
        A.__init__(self)


    def info(self):
        return self.ala


c = C()
print(c.kopnij())
print(c.trenuj())
print(c)
print(c.info())
print(c.bela)


