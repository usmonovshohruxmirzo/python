import math

def calculate_circumference(radius: int) -> float: # Function
    return 2 * math.pi * radius # Operator

class Circle: # class
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return calculate_circumference(self.radius)


# Main block of the program

if __name__ == "__main__": # Control Structure if
    circle = Circle(15)
    print(f"Cirlce circumference: {circle.circumference()}")



print(1)

def func(): # The func() function is not executed because it is not called.
    print(2)


print(3)
# print(__name__)
if __name__ == "__main__":
    func()

print("Html"); print("Css"); print("JS")

# Implicit Line Continuation
person_age = 12
if (
    person_age >= 10 and
    person_age <= 19
):
    print(True)

if 10 <= person_age <= 19:
    print(2, True)

age = \
    1 + 2 \
    + 3 + 4 \
    + 5 + 8

print("age:", age)


# Hash (#)
# An example of a one-line comment.

# Triple Double Quotation
"""
    An example 
    of a multiple-line comment.
"""

class Person:
    def __init__(self, first_came, last_name):
        self.firstName = first_came
        self.lastName = last_name
person = Person("Hello", "hello")
print(person.firstName)