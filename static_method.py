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

    @property # The @property decorator is used to define a property for the brand attribute. It allows you to access the brand attribute as if it were a regular attribute, while still providing the ability to define custom behavior for getting and setting its value. In this case, it provides a getter method for the brand attribute, allowing you to retrieve its value using car_instance.brand instead of car_instance.get_brand().
    def brand(self):
        return self.__brand  # Getter method for brand
    
    @brand.setter # The @brand.setter decorator is used to define a setter method for the brand property. It allows you to set the value of the brand attribute using car_instance.brand = new_value instead of car_instance.set_brand(new_value). This provides a more intuitive and Pythonic way to work with the brand attribute while still allowing for custom behavior when setting its value.
    def brand(self, brand):
        self.__brand = brand  # Setter method for brand

    @staticmethod # The @staticmethod decorator is used to define a static method that does not take the instance (self) or class (cls) as the first argument. This allows the method to be called on the class itself or on an instance of the class without needing to access any instance or class-level attributes.
    def peep():
        print("Peeping at the car!")

    @classmethod # The @classmethod decorator is used to define a class method that takes the class itself as the first argument (car_class) instead of an instance of the class. This allows the method to access and modify class-level attributes, such as cars_count, without needing to create an instance of the class.
    def countcars(car_class):
        return car_class.cars_count
        #print(f"Total number of cars created: {car_class.cars_count()}")  # Accessing the class method to get the total number of Car instances created

    
    """
    The __str__ method is a special method in Python that is used to define the string representation of an object. 
    When you call the str() function on an object or use the print() function to display the object, Python will call 
    the __str__ method to get a human-readable string representation of the object. In this case, it returns a formatted 
    string that includes the brand, year, color, model, and price of the Car instance. 
    This makes it easier to understand the contents of the object when printed or converted to a string.
    """
    def __str__(self):  
        return f"Car(brand={self.__brand}, year={self.__year}, color={self.__color}, model={self.__model}, price={self.__price})"  # String representation of the Car instance

    def __repr__(self): # 
        return f"Car(brand={self.__brand}, year={self.__year}, color={self.__color}, model={self.__model}, price={self.__price})"  # Official string representation of the Car instance

    def print_car_details(self):  # Method to print the details of the Car instance
        print(f"Brand: {self.__brand}, Year: {self.__year}, Color: {self.__color}, Model: {self.__model}, Price: ${self.__price}")  # Print the details of the Car instance

car1 = Car("Toyota", 2020, "Red", "Camry", 25000)  # Creating an instance of the Car class
car1.peep()  # Calling the static method peep() using the instance car1
car2 = Car("Honda", 2021, "Blue", "Civic", 22000)  # Creating another instance of the Car class
car2.peep()  # Calling the static method peep() using the instance car2
Car.peep()  # Calling the static method peep() using the class name Car
car1.print_car_details()  # Calling the method to print the details of car1
car2.print_car_details()  # Calling the method to print the details of car2