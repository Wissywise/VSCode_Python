class Car:
    def __init__(self, brand, year, color, model, price): # Constructor method to initialize the attributes of the Car class
        self.__brand = brand  # Instance variable
        self.__year = year
        self.__color = color
        self.__model = model
        self.__price = price

    def set_brand(self, brand):
        self.__brand = brand  # Setter method for brand

    def get_brand(self):
        return self.__brand  # Getter method for brand

    number_of_wheels = 4  # Class variable

car1 = Car("Toyota", 2020, "Red", "Camry", 25000)  # Creating an instance of the Car class
car2 = Car("Honda", 2021, "Blue", "Civic", 22000)  # Creating another instance of the Car class
print(f"Car 1: {car1.get_brand()}, {car1._Car__year}, {car1._Car__color}, {car1._Car__model}, ${car1._Car__price}")  # Accessing instance variables of car1
print(f"Car 2: {car2.get_brand()}, {car2._Car__year}, {car2._Car__color}, {car2._Car__model}, ${car2._Car__price}")  # Accessing instance variables of car2
car1.set_brand("Nissan")  # Modifying the brand of car1 using the setter method
print(f"Updated Car 1 Brand: {car1.get_brand()}")  # Accessing the updated brand of car1 using the getter method