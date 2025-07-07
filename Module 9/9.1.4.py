"""Классы ArithmeticProgression и GeometricProgression
Реализуйте класс ArithmeticProgression для генерации членов арифметической прогрессии. При создании экземпляра класса ArithmeticProgression должны указываться первый член последовательности и разность прогрессии:

progression = ArithmeticProgression(0, 1)

for elem in progression:
    if elem > 10:
        break
    print(elem, end=' ')    # 0 1 2 3 4 5 6 7 8 9 10
Обратите внимание, что арифметическая прогрессия должна быть итерируемой, а также бесконечной.

Аналогичным образом реализуйте класс GeometricProgression для генерации членов геометрической прогрессии. При создании экземпляра класса GeometricProgression должны указываться первый член последовательности и знаменатель прогрессии:

progression = GeometricProgression(1, 2)

for elem in progression:
    if elem > 10:
        break
    print(elem, end=' ')    # 1 2 4 8
Геометрическая прогрессия, как и арифметическая, должна быть итерируемой, а также бесконечной.

Тестовые задания: https://github.com/python-generation/OOP/tree/main/Module_9/Module_9.1/Module_9.1.4"""

class ArithmeticProgression:
    def __init__(self, first: int, step: int) -> None:
        self.first = first
        self.step = step

    def __iter__(self):
        return self

    def __next__(self) -> int:
        value = self.first
        self.first += self.step
        return value

class GeometricProgression(ArithmeticProgression):
    def __next__(self) -> int:
        value = self.first
        self.first *= self.step
        return value