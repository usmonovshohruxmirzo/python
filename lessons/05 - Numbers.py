# Python Numbers

# There are three numeric types in Python:

# int
# float
# complex


x = 1 # Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
y = 2.5 # Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
z = 3j # Complex numbers are written with a "j" as the imaginary part:

print(x, type(x))
print(y, type(y))
print(z, type(z))

# Type Conversion

print(float(x))
print(int(y))
print(complex(x))

# Random Number
import random

print(random.randrange(1, 10))