# Comprehensions 

# List Comprehension
# Syntax
# [expression for item in iterable if condition]

# Basic Transformation:
# numbers = [1, 2, 3, 4, 5]
# squares = [x ** 2 for x in numbers]
# print(squares)

# With Condition:
# evens = [x for x in numbers if x % 2 == 0]
# print(evens)

# Nested Loops:
# matrix = [[1, 2], [3, 4]]
# flat_list = [num for row in matrix for num in row]
# print(flat_list)

# Dictionary Comprehension
# Syntax
# {key_expression: value_expression for item in iterable if condition}

# Basic Transformation:
# numbers = [1, 2, 3]
# squares = {x: x ** 2 for x in numbers}
# print(squares)

# With Condition:
# cubes = {x: x ** 3 for x in numbers if x % 2 == 1}
# print(cubes)

# Transforming Existing Dictionaries:
# old_dict = {"a": 1, "b": 2, "c": 3}
# new_dict = {key.upper(): value * 2 for key, value in old_dict.items()}
# print(new_dict)


# Set Comprehension
# Syntax:
# {expression for item in iterable if condition}

# Basic Transformation:
numbers = [1, 2, 2, 3, 3, 4]
unique_squares = {x ** 2 for x in numbers}
print(unique_squares)

# With Condition:
evens = {x for x in numbers if x % 2 == 0}
print(evens)

# Nested Comprehensions
matrix = [[1, 2, 3], [4, 5, 6]]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transpose)

# Generator Expressions (Similar to Comprehensions)
numbers = [1, 2, 3, 4, 5]
squared_gen = (x ** 2 for x in numbers)
print(next(squared_gen))
print(next(squared_gen))
print(next(squared_gen))