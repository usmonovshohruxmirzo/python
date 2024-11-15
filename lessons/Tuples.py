# ========================= Tuples

# Key characteristics of tuples:
# Ordered Collection
#   Tuples maintain the order of elements, allowing you to access elements by position.
# Immutability
#   Tuples are immutable, meaning that after a tuple is created, it cannot be modified. This ensures the integrity of data.
# Heterogeneous Elements
#   Tuples can contain elements of various data types, including other tuples.
# Fixed Size
#   Once a tuple is created, its size cannot change, which can improve performance compared to lists in certain situations.

# Creating an empty tuple
empty_tuple = ()

# Creating a tuple with integers
int_tuple = (1, 2, 3, 4, 5)

# Creating a tuple with mixed data types
mixed_tuple = (1, "two", 3.0, (4, 5))
print(mixed_tuple)
# Creating a tuple without parentheses
implicit_tuple = 1, 2, 3

# Creating a single-element tuple (note the comma)
single_element_tuple = (1,)

# Tuple Immutability
# my_tuple = (1, 2, 3)
# my_tuple[1] = "Hello" # Raises TypeError: 'tuple' object does not support item assignment

# Packing and Unpacking
# Unpacking
(a, b, c) = (1, 2, 3)
print(a, b, c)

my_tuple = 40, 56.6, 90
print(my_tuple)
print(*my_tuple)

# Packing and
a, b, c = 40, 56.6, 90

# Swapping Two Values
a, b = 1, 2
print(a, b)
temp = a
a = b
b = temp
print(a, b)

# The Solution Using Unpacking and Packing
a, b = 1, 2
print(a, b)
b, a = a, b
print(a, b)


# "==" And "is" Operators
x = (1, 2, 3)
y = (1, 2, 3)
print(x == y)
print(id(x), id(y))
print(x is y)

# id() - In Python, id() gives the memory address of an object.
# The value from id() changes every run because Python may allocate memory differently each time a script is executed. Memory addresses aren't fixed between runs, and id() reflects these addresses.