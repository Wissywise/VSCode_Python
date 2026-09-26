class Vehicle():
    def __init__(self, brand, year, color, model, price): # Constructor method to initialize the attributes of the Vehicle class
        self.__brand = brand  # Instance variable
        self.__year = year
        self.__color = color
        self.__model = model
        self.__price = price

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        self.__brand = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

class Car(Vehicle):  # Inheriting from the Vehicle class
    number_of_wheels = 4  # Class variable

    def __init__(self, brand, year, color, model, price):
        super().__init__(brand, year, color, model, price)  # Call the constructor of the parent class (Vehicle)

car1 = Car("Toyota", 2020, "Red", "Camry", 25000)  # Creating an instance of the Car class
print(car1.brand)  # Accessing the brand attribute using the property
print(car1.year)   # Accessing the year attribute using the property
print(car1.color)  # Accessing the color attribute using the property
print(car1.model)  # Accessing the model attribute using the property
print(car1.price)  # Accessing the price attribute using the property