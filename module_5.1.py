#Цель: применить на практике знания о классах, объектах и их атрибутах.
#Задача "Developer - не только разработчик":
#Реализуйте класс House, объекты которого будут создаваться следующим образом:
#House('ЖК Эльбрус', 30)
#Объект этого класса должен обладать следующими атрибутами:
#self.name - имя, self.number_of_floors - кол-во этажей
#Также должен обладать методом go_to(new_floor), где new_floor - номер этажа(int),
# на который нужно приехать.
#Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно).
#Если же new_floor больше чем self.number_of_floors или меньше 1,
# то вывести строку "Такого этажа не существует".

class House:
    def __init__(self,name,number_of_floors ):
        self.name = name
        self.number_of_floors  = number_of_floors
        self.say_house()

    def say_house(self):
        print(f'Название - {self.name}, количество этажей - {self.number_of_floors}')

h1 = House("ЖК Горский", 18)
h2 = House("Домик в деревне", 2)
