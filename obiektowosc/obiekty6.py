# Zaimplementuj klase Vector dostarczajaca funkcjonalnosc wektora
# swobodnego na dwuwymiarowej płaszczyznie. Wektory powinny
# miec mozliwosc dodawania, odejmowania, mnozenia (przez liczbe),
# porównywania (po długosci) oraz powinny posiadac czytelna
# reprezentacje napisowa.
# Przykład uzycia:
# vector_1 = Vector(x=1, y=2)
# vector_2 = Vector(x=1, y=2)
# vector_3 = vector_1 + vector_2

class Vector:
    def __init__(self, x:int, y:int):
        self._x = x
        self._y = y

    def len(self):
        return (self._x ** 2 + self._y ** 2) ** (1/2)

    def __str__(self):
        return f'Vector: x={self._x}, y={self._y}'

    def __add__(self, other):
        if type(other) == type(self):
            return Vector(self._x + other._x, self._y + other._y)

    def __sub__(self, other):
        if type(other) == type(self):
            return Vector(self._x - other._x, self._y - other._y)

    def __mul__(self, other):
        if type(other) == int:
            return Vector(self._x * other, self._y*other)

    def __ge__(self, other):
        return self > other or self == other

    def __gt__(self, other):
        if type(other) == type(self):
            return self.len() > other.len()

    # def __le__(self, other):
    #     return True
    #
    # def __lt__(self, other):
    #     return True

    def __eq__(self, other):
        if type(other) == type(self):
            return self.len() == other.len()

    def __ne__(self, other):
        return not self == other



a = Vector(x=1, y=2)
b = Vector(x=4, y=9)
c = a+b
d = Vector(-1,2)

print(c)

c = a - b
print( c._x, c._y)

print(a < b)
# print(a == d)
# print(a != d)
# print(a == c)
# print(a != c)
# # print(a>b)
