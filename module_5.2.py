# Цель: понять как работают базовые магические методы на практике.
#  Задача "Магические здания":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче.
# Необходимо дополнить класс House следующими специальными методами:
# __len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
# __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".

class House:
    def __init__(self, name, number_of_floors, new_floor):
        self.name = name
        self.number_of_floors = number_of_floors
        self.new_floor = new_floor

    #    self.say_house()
    #    self.go_to()

    def say_house(self):
        print(f'Название - {self.name}, количество этажей - {self.number_of_floors} ')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    # def go_to(self):
    #     floor = 0
    #     print(f'Объект - {self.name} имеет {self.number_of_floors} этажей \nХотим подняться на {self.new_floor}-й')
    #     if self.new_floor < 1 or self.new_floor > self.number_of_floors:
    #         print(f'Такого этажа не существует')
    #     else:
    #         for floor in range(self.new_floor):
    #             print(floor + 1)


h1 = House("ЖК Горский", 18, 5)
h2 = House("Домик в деревне", 2, 10)

print(h1)
print(h2)

print(len(h1))
print(len(h2))
