# Container data: List, Tuple, Dict, Set



# ========================= Lists
# Key characteristics of lists:
# Ordered collection
#   The elements in a list have a defined order, which means each element has a specific position or index.
# Mutability
#   Lists are mutable, meaning their elements can be modified, including by adding, removing, or changing elements.
# Heterogeneous elements
#   A list can contain elements of different data types.
# Dynamic Size
#   Lists can grow and shrink in size as needed, accommodating dynamic data needs.

# Creating an empty list
empty_list = []

# Creating a list with integers
int_list = [1, 2, 3, 4, 5]

# Creating a list with mixed data types
mixed_list = [1, "two", 3.0, [4, 5]]

# Creating a list using the list constructor
constructed_list = list((1, 2, 3))

my_list = ['apple', 'banana', 'cherry']

# Accessing the first element
first_element = my_list[0]  # Output: 'apple'

# Accessing the last element
last_element = my_list[-1]  # Output: 'cherry'

my_list.append("asdasdasdsadas")
my_list[1] = False
print( my_list)

some_numbers = [1, 3, 5, 9, 11, 16, 28, 44.7, 90.6, 5334]
for i in some_numbers[::2]:
    print(i)

"""
    The first : means "start at the beginning" (default).
    The second : indicates "end at the end" (default).
    The 2 after the second : specifies the step, meaning it selects every second element.
"""

# sort()
nums = [5,6,8,2,4,9,6,7,12]
nums.sort()
print(nums)

# len()
print("Length:", len(nums))

# extend() -  The extend method allows you to add all the items from another iterable object, for example, from another list or string.
some_list = [1, 2, 3]
some_str = "abc"
some_list.extend(some_str)
print(some_list)

# count
x = 1
some_list = [1, 2, 3, 2, 1, 1]
print(f"({x}) - {some_list.count(x)}")

# pop() - The pop method allows the items from a list to be removed and returned using the given index. If an index is not specified, pop removes and returns the last item in a list. This method allows a list to be used as a stack.
my_stack = [1, 2, 3]
my_stack.append(4)
my_stack.append(5)
print(my_stack)
print("removed", my_stack.pop())
print("removed", my_stack.pop())
print(my_stack)
print("removed", my_stack.pop(0))
print(my_stack)


# List Comprehensions
# Possible standard solution
# n = int(input("Input integer number: "))
# even_numbers = []
# for i in range(1, n):
#     if not i % 2:
#         even_numbers.append(i)
#
# print(even_numbers)

# Solution with List Comprehensions
# n = int(input("Input integer number: "))
# even_numbers = [i for i in range(1, n) if not i % 2]
# print(even_numbers)

# a = ""
# for i in range(3, 7):
#     a += f"{i:2}"
# print(a)
#
# array = [1,"JS", True, {}, [], None]
# print(array)
#
# print(len(array))
#
# print(type(array))
#
# # The list() Constructor
# the_list = list((1, 2, 3))
# print(the_list)
#
# print(array[1])
# print(array[-1]) # last item of the list
# print(array[2:5]) # Note: The search will start at index 2 (included) and end at index 5 (not included).
# print(array[:4])
# print(array[2:])
# print(array[-4:-1])
#
# if "JS" in array:
#     print("JS", True)


# methods

# append
test_array = [1, 2, 3, 4]
test_array.append([10]) # adds new element last of the array
test_array[len(test_array):] = [20]
print("append()", test_array)

# extend
test_array = [1, 2, 3, 4]
test_array.extend(["hello", "css", (1, 2), {}])
print("extend()", test_array)

# insert
test_array = [1, 2, 3, 4]
test_array.insert(1, "hello")
print("insert()", test_array)

# remove
test_array = [1, 2, 3, 4, "html"]
test_array.remove("html")
print("remove()", test_array)

# pop
test_array = [1, 2, 3, 4]
test_array.pop() # remove from last el
test_array.pop(1) # removes by index
print("pop()", test_array)

# clear
test_array = [1, 2, 3, 4]
# test_array.clear()
del test_array[:] # this Equivalent to clear()
print("clear()", test_array)