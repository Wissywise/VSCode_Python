class Vehicle():
    def __init__(self, color, model, year):
        self.__color = color
        self.__model = model
        self.__year = year


    def print_veh(self):
        print('Hello, I am a vehicle')


class Factory():
    def __init__(self):
        pass

    def print_factory(self):
        print('This is the factory')

class Car(Vehicle, Factory):
    pass

car1 = Car('Red', 'BMW', 2026)
car1.print_veh()
car1.print_factory()
            