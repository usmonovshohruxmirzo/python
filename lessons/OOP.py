from docutils.nodes import title, author


class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color
    
    def drive(self):
        print(f"{self.model} is driving")

my_car = Car("BMW", "red")
my_car.drive()

# Encapsulation

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute
        self.account_name = "Usmonov Shoxruxmirzo"

    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance()) 
print(account.account_name)

# Inheritance

# class Animal:
#     def eat(self, name):
#         print(name, "This animal eats food.")

# class Dog(Animal):
#     def bark(self):
#         print("Dog Barks")

# dog = Dog()
# dog.eat("Alex")
# dog.bark()

# Polymorphism

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        print("Area of Circle")

class Square(Shape):
    def area(self):
        print("Area of Square")

shape1 = Circle()
shape2 = Square()

shape1.area()
shape2.area()

# Abstraction

from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract class
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog barks.")

dog = Dog()
dog.sound()  

# Association
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # Association (Composition)

    def drive(self):
        self.engine.start()

car = Car()
car.drive()

"""
Advantages of OOP:
Modularity: Code is organized into classes.
Reusability: Inheritance promotes code reuse.
Scalability: Easy to add new features.
Maintainability: Encapsulation simplifies debugging and updates.
"""

"""
__str__: Returns a user-friendly string representation of the object (e.g., for print()).
__repr__: __repr__ shows the object’s representation as a string, usually for debugging. It gives a detailed view of the object's key attributes.
__len__: Returns the length of the object (e.g., for len()).
__add__, __sub__, etc.: Support for operator overloading (e.g., +, -).
"""
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r}, pages={self.pages!r})"

    def __len__(self):
        return self.pages
    

book = Book("1984", "George Orwell", 328)
print(str(book))
print(len(book))
print(repr(book))

#! Class Methods and Static Methods

"""
*@classmethod:
Takes the class (cls) as the first argument.
Can access and modify class-level attributes and methods.
Often used for factory methods or class-level operations.
Example:
"""
class Dog:
    species = "Canine"  # Class-level attribute
    
    def __init__(self, name):
        self.name = name  # Instance-level attribute

    @classmethod
    def get_species(cls): # cls is class Dog
        return cls.species  # Accesses class-level attribute

    @classmethod
    def create_dog(cls, name):
        return cls(name)  # Creates a Dog instance using the class method

dog1 = Dog.create_dog("Buddy")
print(dog1.name)  # Output: Buddy

print(Dog.get_species())  # Output: Canine

"""
*@staticmethod
No access to class or instance.
Works like a regular function but belongs to the class.
Doesn't take self or cls as its first argument.


The purpose of @classmethod is to allow methods to work with the class itself (via cls), rather than a specific instance. It’s mainly used for:
Creating instances using alternative constructors.
Accessing or modifying class-level data.
"""

class Math:
    @staticmethod
    def add(a, b):
        return a + b
    
print(Math.add(5, 7)) 

"""
Key Difference:
    *@staticmethod: Doesn't access the class or instance.
    *@classmethod: Accesses the class itself (cls).
"""


#  Properties (@property, setter)

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):  # Getter
        return self._celsius

    @celsius.setter
    def celsius(self, value):  # Setter
        if value < -273.15:
            raise ValueError("Temperature cannot go below -273.15°C")
        self._celsius = value

    @property
    def fahrenheit(self):  # Read-only derived property
        return (self._celsius * 9/5) + 32
 
temp = Temperature(25) #  Creates an object with _celsius = 25
print(temp.celsius) # Calls the getter: returns _celsius = 25
temp.celsius = 50 # Calls the setter: changes _celsius to 50
print(temp.celsius) # Calls the getter: returns _celsius = 50

"""
When you write temp.celsius, Python automatically calls the getter method:
Without @property, a method stays a regular function, so you must use () to call it.
"""