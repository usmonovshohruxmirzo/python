# ==================== Python Variables

# x = 5
# y = "Hello"
# print(x)
# print(y)

#  Variable Names
# myvar = "hello"
# my_var = "hello"
# _my_var = "hello"
# MYVAR = "hello"
# myvar = "hello"

# Assign Multiple Values

# x, y, z = "1", "2", "3"
# print(x)
# print(y)
# print(z)

# a = b = c = "a,b,c"
# print(a)
# print(b)
# print(c)

# Unpack a Collection
# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x, y, z)


# Output Variables

# x = "Python"
# y = "is"
# z = "awesome"
# print(x, y, z)
# print(x + y + z)

# x = 5
# y = 10
# print(x + y)

# Global Variables

# x = "awesome"

# def myFunc():
#     x = "fantastic"
#     print("Python is " + x)

# myFunc()

# print("Python is " + x)

# If you use the global keyword, the variable belongs to the global scope:

# def myFunc():
#     global x
#     x = "Great"
# myFunc()

# print("Python is " + x)

x = "awesome"

def myFunc():
    global x
    x = "fantastic"
    print("Python is " + x)

myFunc()

print("Python is " + x)