class Vehicle:
    def __init__(self, brand, year, color, model, price):  # Constructor method to initialize the attributes of the Vehicle class
        self.__brand = brand  # Instance variable
        self.__year = year
        self.__color = color
        self.__model = model
        self.__price = price

    def get_brand(self):
        print(f"Brand: {self.__brand}")  # Getter method for brand

class Car(Vehicle):  # Inheriting from the Vehicle class
    number_of_wheels = 4  # Class variable
    def __init__(self, brand, year, color, model, price):
        super().__init__(brand, year, color, model, price)  # Call the constructor of the parent class (Vehicle)
        print(f"Car created: {self.__brand}, {self.__year}, {self.__color}, {self.__model}, ${self.__price}")  # Print the attributes of the Car instance

    def car_with_wheel(self): # 
        print(f"Car with wheel: {self.__brand}, {self.__model}, {self.number_of_wheels}") # Print details with wheel

    """
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
    """