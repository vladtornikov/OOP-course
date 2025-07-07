"""Класс Vector
Реализуйте класс Vector, экземпляр которого представляет собой вектор произвольной размерности. Экземпляр класса Vector должен создаваться на основе собственных координат:

a = Vector(1, 2, 3)
b = Vector(3, 4, 5)
c = Vector(5, 6, 7, 8)
В качестве неформального строкового представления вектор должен иметь собственные координаты, заключенные в круглые скобки:

print(a)                       # (1, 2, 3)
print(b)                       # (3, 4, 5)
print(c)                       # (5, 6, 7, 8)
Векторы должны поддерживать между собой операции сложения, вычитания, произведения и нормирования:

print(a + b)                   # (4, 6, 8)
print(a - b)                   # (-2, -2, -2)
print(a * b)                   # 1*3 + 2*4 + 3*5 = 26
print(c.norm())                # sqrt(5**2 + 6**2 + 7**2 + 8**2) = sqrt(174) = 13.19090595827292
а также операции сравнения на равенство и неравенство:

print(a == Vector(1, 2, 3))    # True
print(a == Vector(4, 5, 6))    # False
При попытке выполнить какую-либо операцию с векторами разной размерности должно быть возбуждено исключение ValueError с текстом:

Векторы должны иметь равную длину"""

from __future__ import annotations
from math import sqrt


class Vector:
    def __init__(self, *args: int):
        self.elements = args

    def __str__(self):
        return f'{self.elements}'

    def __add__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            return NotImplemented
        Vector.check_length(self.elements, other.elements)
        return Vector(*[sum(el) for el in zip(self.elements, other.elements)])

    def __sub__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            return NotImplemented
        Vector.check_length(self.elements, other.elements)
        return Vector(*[el[0] - el[1] for el in zip(self.elements, other.elements)])

    def __mul__(self, other: Vector) -> int:
        if not isinstance(other, Vector):
            return NotImplemented
        Vector.check_length(self.elements, other.elements)
        return sum([el[0] * el[1] for el in zip(self.elements, other.elements)])

    def norm(self) -> float:
        return sqrt(sum(pow(el, 2) for el in self.elements))

    def __eq__(self, other) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        Vector.check_length(self.elements, other.elements)
        return self.elements == other.elements

    @staticmethod
    def check_length(first: tuple[int], second: tuple[int]):
        if len(first) != len(second):
            raise ValueError('Векторы должны иметь равную длину')