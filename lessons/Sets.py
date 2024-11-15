# Key characteristics of sets:
#   Unordered Collection
#       The elements of a set have no specific sequence, meaning they cannot be accessed by position.
#   Unique Elements
#       Sets automatically ensure that all elements are unique. If duplicate elements are added to a set, they are ignored, which is useful for deduplication tasks.
#   Mutability
#       Sets are mutable, meaning you can add or remove elements after creating a set. However, the elements themselves (e.g., numbers, strings, or tuples) must be immutable.
#   Heterogeneous Elements
#       Sets can contain elements of different data types if they are immutable.
#   Efficient Membership Testing
#       Sets provide highly efficient membership testing (checking if an element is in a set) with an average time complexity of O(1).
#   Support for Mathematical Operations
#       Sets support mathematical operations such as union, intersection, difference, and symmetric difference, which are useful for comparing and combining sets.
#   Dynamic Size
#       The size of a set can change dynamically as elements are added or removed. This flexibility allows sets to adjust to varying data sizes without explicit resizing.
from lessons.Lists import some_list

# In Python, you cannot create an empty set using curly braces {} because they are used to define dictionaries. If you try to use {} to create an empty set, Python will interpret it as an empty dictionary instead.
# To create an empty set, the set() constructor can be used. An empty set can be created as follows:

empty_set = set()
print(empty_set)
print(type(empty_set))

empty_set_2 = {}
print(type(empty_set_2))

my_set = set((1, 113.5, True, "Some string"))
print(my_set)
print(type(my_set))

my_set = {1, 113.5, True, "Some string"}
print(type(my_set))

my_set = set([1, 2, 3, 1, 2]) # sets cannot contain duplicates.
print(my_set)

for i in my_set: # sets are iterable
    print(i)

# but you cannot access directly with index
# print(my_set[1]) # TypeError: 'set' object is not subscriptable

# You can also check the membership and length of a set.
if 1 in my_set:
    pass
print("passed")
print(len(my_set))

# Hashable Objects
# Everything in Python is an object. So, an object in Python is considered hashable if the class of the object implements a few special methods that produce a hash value.
# A hash value is an integer value that uniquely identifies data.

some_tuple = (1, 2, 3)
print(hash(some_tuple))

some_list = [1, 2, 3]
# print(hash(some_list)) # TypeError: unhashable type: 'list'

# Set Operations
# union()
# set_1 = {"a", "d", "h"}
# set_2 = {"n", "b", "c", "d"}
# set_3 = {"c", "d"}
# union = set_1 | set_2 | set_3
# print(union)
# or
# union_2 = set_1.union(set_2, set_3)
# print(union_2)

# intersection
# set_1 = {"a", "d", "h"}
# set_2 = {"a", "b", "c", "d"}
# set_3 = {"c", "d", "a"}
# my_intersection = set_1 & set_2 & set_3
# print(my_intersection)
# or
# my_intersection_2 = set_1.intersection(set_2, set_3)
# print(my_intersection_2)

# difference()
set_1 = {"a", "d", "h"}
set_2 = {"a", "b", "c", "d"}
set_3 = {"c", "d", "a"}
my_difference = set_1 - set_2 - set_3
print(my_difference)
# or
my_difference_2 = set_1.difference(set_2, set_3)
print(my_difference_2)

# Update Method
s1 = {"a", "b", "k"}
s2 = {"a", "d", "h"}
s3 = {"n", "b", "d"}
s1.update(s2, s3)
print(s1)

# Add and Remove Methods
new_set = {"html", "css", "js"}
new_set.add("react")
new_set.add("angular")
print(new_set)
new_set.remove("css")
print(new_set)

# clear()
new_set.clear()
print(new_set)