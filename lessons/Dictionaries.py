# Dictionaries
# Key characteristics of dictionaries:
#   Key-Value Pairs
#     Dictionaries store data in key-value pairs, allowing you to map keys to their corresponding values efficiently.
#   Unordered Collection
#     The elements in a dictionary are not ordered. In Python 3.7 and later, dictionaries maintain insertion order, but you should not count on this behavior for all use cases.
#   Mutability
#     Dictionaries are mutable, meaning you can add, remove, or change key-value pairs after creating a dictionary.
#   Unique Keys
#     The keys in a dictionary must be unique. If you add a key that already exists, the old value is overwritten with the new value.
#   Heterogeneous Keys and Values
#     Both keys and values in a dictionary can be of any data type, allowing for flexible data storage.
#   Efficient Lookups
#     Dictionaries provide an average time complexity of O(1) for lookups, insertions, and deletions based on keys, making them highly efficient for fast data retrieval.
#   Dynamic Size
#     The size of a dictionary can change dynamically as key-value pairs are added or removed, which provides flexibility in managing varying amounts of data.
#   Hashable Keys
#     Keys must be hashable, meaning they must be of immutable data types like strings, numbers, or tuples, which ensures they are unique and can be accessed quickly.
#   Support for Iteration
#     Dictionaries support efficient iteration over keys, values, or key-value pairs, which is useful for processing or manipulating their contents.


obj = {
    "name": "Filip",
    "age": 32,
    "is_registered": False,
    "rate": 12.5,
    "total_score": 200,
    "linked_ids": [1, 45, 98]
}
print(obj)
print(type(obj))

obj_2 = dict([(1, "Alex"), (2, "Anna")])
print(obj_2)

# access
name = obj["name"]
print(name)

# update
obj["age"] = 777
print(obj)

# delete
del obj["age"]
print(obj)

# iteration
for item in obj.items():
    print(item)

if "preferences" in obj and obj["preferences"]:
    print(obj["preferences"])
else:
    print("404")

# Dictionary Manipulations
print("Dictionary Manipulations")
# get()
print(obj.get("rate", "There is nothing!"))
# items()
for item in obj.items():
    print(item)
# values()
for value in obj.values():
    print("value:", value)
# keys()
for key in obj.keys():
    print("key:", key)
# update
uncompleted_obj = {
    "name": "",
    "age": 0,
    "is_registered": False,
    "rate": 0,
    "total_score": 0,
    "linked_ids": []
}
uncompleted_obj.update([
    ("name", "Alex"),
    ("age", 25),
    ("rate", 10.5),
    ("total_score", 158.52)
])
print(uncompleted_obj)