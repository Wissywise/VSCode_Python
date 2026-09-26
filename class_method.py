"""
class Car:
    cars_count = 0  # Class variable to keep track of the number of Car instances

    def __init__(self, brand, year, color, model, price):
        self.__brand = brand
        self.__year = year
        self.__color = color
        self.__model = model
        self.__price = price
        Car.cars_count += 1  # Increment the class variable when an instance of the class is created

    @classmethod
    def get_cars_count(cls):
        return cls.cars_count

car1 = Car("Toyota", 2020, "Red", "Camry", 25000)
car2 = Car("Honda", 2021, "Blue", "Civic", 22000)
print(f"Total number of cars created: {Car.get_cars_count()}")  # Accessing the class method to get the total number of Carinstances created
"""


"""
class Car:
    cars_count = 0  # Class variable to keep track of the number of Car instances

    def __init__(self, color):
        self.__color = color
        Car.cars_count += 1  # Increment the class variable when an instance of the class is created

    @classmethod
    def countcars(car_class):
        return car_class.cars_count

        print(f"Total number of cars created: {Car.countcars()}")  # Accessing the class method to get the total number of Car instances created


car1 = Car("Red")
car2 = Car("Blue")

print(f"Total number of cars created: {Car.countcars()}")  # Accessing the class method to get the total number of Car instances created

"""


"""
class Car:
    cars_count = 0  # Class variable to keep track of the number of Car instances

    def __init__(self, color):
        self.__color = color
        Car.cars_count += 1  # Increment the class variable when an instance of the class is created

    @classmethod
    def countcars(car_class):
        return car_class.cars_count
        #print(f"Total number of cars created: {car_class.cars_count()}")  # Accessing the class method to get the total number of Car instances created


car1 = Car("Red")
car1.countcars()
car2 = Car("Blue")
car2.countcars()

print(f"Total number of cars created: {Car.countcars()}")  # Accessing the class method to get the total number of Car instances created

"""


#"""
class Car:
    cars_count = 0  # Class variable to keep track of the number of Car instances
    def __init__(self, brand, year, color, model, price): # Constructor method to initialize the attributes of the Car class
        self.__brand = brand  # Instance variable
        self.__year = year
        self.__color = color
        self.__model = model
        self.__price = price
        #Car.cars_count += 1  # Increment the class variable when an instance of the class is created
        Car.cars_count = Car.cars_count + 1  # Increment the class variable when an instance of the class is created

    number_of_wheels = 4  # Class variable

    @property
    def brand(self):
        return self.__brand  # Getter method for brand
    
    @brand.setter
    def brand(self, brand):
        self.__brand = brand  # Setter method for brand

    @classmethod
    def count_cars(car_class):
        #return car_class.cars_count
        print(f"Total number of cars created: {car_class.cars_count} Cars ")  # Accessing the class method to get the total number of Car instances created

car1 = Car("Toyota", 2020, "Red", "Camry", 25000)  # Creating an instance of the Car class
car2 = Car("Honda", 2021, "Blue", "Civic", 22000)  # Creating another instance of the Car class
car1.brand = "Nissan"  # Modifying the brand of car1 using the setter method
print(f"Updated Car 1 Brand: {car1.brand}")  # Accessing the updated brand of car1 using the getter method
Car.count_cars()
#"""