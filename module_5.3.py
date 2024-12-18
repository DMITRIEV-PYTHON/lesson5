# Цель: применить знания о перегрузке арифметических операторов и операторов сравнения.
# Задача "Нужно больше этажей":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Специальные методы класса".
# Необходимо дополнить класс House следующими специальными методами:
# __eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
# Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и возвращать результаты сравнения по соответствующим операторам. Как и в методе __eq__ в сравнении участвует кол-во этажей.
# __add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
# __radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).
# Остальные методы арифметических операторов, где self - x, other - y:

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):  # сравнение,если количество этажей = (равно) TRUE
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            # проверяет, является ли объект экземпляром указанного класса и его тип соответствует INT
            return self.number_of_floors == other.number_of_floors

    def __le__(self, other):  # сравнение,если количество этажей <= TRUE
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            # проверяет, является ли объект экземпляром указанного класса и его тип соответствует INT
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):  # сравнение,если количество этажей > TRUE
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            # проверяет, является ли объект экземпляром указанного класса и его тип соответствует INT
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):  # сравнение,если количество этажей >= TRUE
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            # проверяет, является ли объект экземпляром указанного класса и его тип соответствует INT
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):  # сравнение,если количество этажей != (не равно) TRUE
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            # проверяет, является ли объект экземпляром указанного класса и его тип соответствует INT
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):  # изменение количества этажей
        if isinstance(value, int):  # проверяем, тип объекта соответствует INT
            self.number_of_floors = self.number_of_floors + value
            return self

    def __radd__(self, value):  # изменение количества этажей
        # метод __radd__ метод вызывается для реализации арифметических операций с отраженными (переставленными)
        # операндами. Эти функции вызываются только в том # случае, если левый операнд не поддерживает
        # соответствующую операцию и операнды имеют разные типы. В данном случае вызываем метод __add__
        return self.__add__(value)

    def __iadd__(self, value):  # изменение количества этажей
        if isinstance(value, int):  # проверяем, тип объекта соответствует INT
            # Если в методе __add__ создается новый объект класса House, тогда как при операции +=
            # этого делать не обязательно. мы здесь не создаем нового объекта, а значение в текущем.
            # Это логичнее, так как вызывать цепочкой операцию += не предполагается и, кроме того, она изменяет
            # (по смыслу) состояние текущего объекта.
            self.number_of_floors += value
            return self


h1 = House("ЖК ЭЛЬБРУС", 10)
h2 = House("ЖК АКАЦИЯ", 20)

print(h1)  # выводим название и количество этажей
print(h2)

print(h1 == h2, "(проверка равенства - 10 не равно 20)")  # результат "равно"

h1 = h1 + 10
print(h1)  # добавили 10 этажей ЖК "ЭЛЬБРУС" (метод __add__)

print(h1 == h2, "(проверка равенства - 20 равно 20)")  # результат "равно", потому что добавили 10 этажей

h1 += 10
print(h1)  # добавили 10 этажей ЖК "ЭЛЬБРУС" (метод __iadd__)
# print(h1 +=10)  не заработает, необходимо возвращать новый обьект
# мы не можем использовать операторы внутри оператора print, поэтому получаем синтаксическую ошибку.
# x += 1— это расширенный оператор присваивания в Python.

h2 = 10 + h2
print(h2)  # добавили 10 этажей ЖК "АКАЦИЯ" (метод __radd__)

print(h1 > h2, "(30 > 30)")  # результат ">" (__gt__)

print(h1 >= h2, "(30 >= 30)")  # результат ">=" (__ge__)

print(h1 < h2, "(30 < 30)")  # результат "<" (__lt__)

print(h1 <= h2, "(30 <= 30)")  # результат "<=" (__le__)

print(h1 != h2, "(проверка неравенства - 30 равно 30)")  # результат "не равно" (__ne__)
