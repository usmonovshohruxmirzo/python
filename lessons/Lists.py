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