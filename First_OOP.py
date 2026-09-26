class Car:
    def __init__(self, brand, year, color, model, price): # Constructor method to initialize the attributes of the Car class
        self.brand = brand  # Instance variable
        self.year = year
        self.color = color
        self.model = model
        self.price = price
    number_of_wheels = 4  # Class variable
car1 = Car("Toyota", 2020, "Red", "Camry", 25000)  # Creating an instance of the Car class
car2 = Car("Honda", 2021, "Blue", "Civic", 22000)  # Creating another instance of the Car class
print(f"Car 1: {car1.brand}, {car1.year}, {car1.color}, {car1.model}, ${car1.price}")  # Accessing instance variables of car1
print(f"Car 2: {car2.brand}, {car2.year}, {car2.color}, {car2.model}, ${car2.price}")  # Accessing instance variables of car2
print(f"Number of wheels: {Car.number_of_wheels}")  # Accessing class variable

car3 = Car("Ford", 2022, "Black", "Mustang", 30000)  # Creating another instance of the Car class
car4 = Car("Ford", 2022, "Black", "Mustang", 30000)  # Creating another instance of the Car class
print(f"Car 3: {car3.brand}, {car3.year}, {car3.color}, {car3.model}, ${car3.price}")  # Accessing instance variables of car3
print(f"Car 4: {car4.brand}, {car4.year}, {car4.color}, {car4.model}, ${car4.price}")  # Accessing instance variables of car4

print(f'car3 == car4: {car3 == car4}')  # Comparing two instances of the Car class (will return False since they are different objects)
