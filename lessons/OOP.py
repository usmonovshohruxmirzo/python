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