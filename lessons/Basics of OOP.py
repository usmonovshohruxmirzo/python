# Procedural, Functional, and Object-Oriented Approaches

"""
Paradigms are fundamental models or patterns of thinking and problem-solving in a particular field. In programming, they refer to different styles of programming, such as:
1. **Imperative**: Focuses on how to perform tasks using statements and control flow.
2. **Declarative**: Focuses on what to do, describing the desired result without explicitly specifying how to achieve it.
3. **Object-Oriented**: Organizes code into objects that contain data and methods.
4. **Functional**: Treats computation as the evaluation of mathematical functions and avoids changing state or mutable data.
Each paradigm has its own approach to solving problems.
"""

#? The Procedural Approach

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = 5
print("The factorial of", number, "is", factorial(number))

#? The Functional Approach

from functools import reduce

def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)

number = 5
print("The factorial of", number, "is", factorial(number))

# Example of List Processing:
# Using the functional approach to process a list of numbers
   
numbers = [1, 2, 3, 4, 5]
   
# Using map to square each number
squares = list(map(lambda x: x ** 2, numbers))
# Using filter to get even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
# Using reduce to sum all numbers
sum_of_numbers = reduce(lambda x, y: x + y, numbers)

print("Original numbers:", numbers)
print("Squares:", squares)
print("Evens:", evens)
print("Sum:", sum_of_numbers)

#? The Object-Oriented Approach
class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}, new balance is ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}, new balance is ${self.balance}")

    def get_balance(self):
        print(f"Current balance is ${self.balance}")

# Creating an object (instance) of BankAccount
account = BankAccount("Alice", 100)

# Using methods of the object
account.deposit(50)
account.withdraw(30)
account.withdraw(150)
account.get_balance()

#? Principles of OOP
#? Encapsulation
# class Car:
#     def __init__(self, make, model, year):
#         self.__make = make
#         self.__model = model
#         self.__model = year
#
#     def get_make(self):
#         return self.__make
#
#     def set_make(self, make):
#         self.__make = make
#
# car = Car("BMW", "M3", 2024)
# print(car.get_make())
# car.set_make("TESLA")
# print(car.get_make())

#? Inheritance
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        print("Driving")

vehicle = Vehicle("BMW", "M3")
vehicle.drive()

class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year

    def honk(self):
        print("Honking")

car = Car("BMW", "M3", 2024)
car.drive()
car.honk()

#? Polymorphism
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Bark")

class Cat(Animal):
    def speak(self):
        print("Meow")

def make_animal_speak(animal):
    animal.speak()

dog = Dog()
cat = Cat()
make_animal_speak(dog)
make_animal_speak(cat)

#? Abstraction

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

shapes = [Rectangle(3,4), Circle(5)]
for shape in shapes:
    print(shape.area())


#? Relationships Between Classes. Aggregation, Composition, Association
# Relationships Between Classes

# 1. Inheritance
class Animal:
    def speak(self):
        return "I make a sound"

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        return "Woof!"

dog = Dog()
print(dog.speak())  # Output: Woof!

# 2. Association
class Driver:
    def __init__(self, name):
        self.name = name

    def drive(self, car):
        print(f"{self.name} is driving a {car.brand}")

class Car:
    def __init__(self, brand):
        self.brand = brand

driver = Driver("Alice")
car = Car("Tesla")
driver.drive(car)

# 3. Aggregation
class Engine:
    def __init__(self, power):
        self.power = power

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine

engine = Engine("200 HP")
car = Car("Toyota", engine)
print(f"{car.brand} has an engine with {car.engine.power}") 

# 4. Composition
class Engine:
    def __init__(self, power):
        self.power = power

class Car():
    def __init__(self, brand, power):
        self.brand = brand
        self.engine = Engine(power)


car = Car("Ford", "250 HP")
print(f"{car.brand} has an engine with {car.engine.power}")  

# Multiple Inheritance
class Animal:
    def __init__(self, name):
        self.name = name
class Pet:
    def __init__(self, owner):
        self.owner = owner

class Dog(Animal, Pet):
    def __init__(self, name, owner):
        Animal.__init__(self, name)
        Pet.__init__(self, owner)

    def speak(self):
        return f"{self.name} says Woof!"
    
dog = Dog("Buddy", "Alex")
print(dog.speak(), "Owner:", dog.owner)