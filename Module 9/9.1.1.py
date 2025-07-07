'''Задача 9.1.1. Реализуйте функцию anything(), которая возвращает такой объект, результат сравнения с которым
c помощью операторов ==, !=, >, <, >= и <= всегда равен True.

Тестовые задания: https://github.com/python-generation/OOP/tree/main/Module_9/Module_9.1/Module_9.1.1'''

class AlwaysTrue:
    def __eq__(self, other):
        return True

    def __ne__(self, other):
        return True

    def __lt__(self, other):
        return True

    def __le__(self, other):
        return True

    def __gt__(self, other):
        return True

    def __ge__(self, other):
        return True

def anything():
    class_true = AlwaysTrue()
    return class_true