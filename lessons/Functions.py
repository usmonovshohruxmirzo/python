def add(a, b):
    return a + b

print(add(10,10))


# lambada functions
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

square = lambda x: x ** 2
print(square(5))

# Recursion
def recursion(n):
    print(n)
    return 1 if n == 1 else recursion(n - 1)

recursion(10)

# Scope and lifetime of variables (global, nonlocal)
# Local Variables
# Global Variables
# Nonlocal Variables

# Local Variables
# def greet():
#     a = "hello"
#     print("local", a)

# greet()
# print(a) # NameError: name 'a' is not defined

# Global Variables
message = 'Hello'
def greet():
    print('Local', message)
greet()
print('Global', message)


# nonlocal Keyword -  Make a function inside a function, which uses the variable x as a non local variable:
def outer():
    message = "local"  # outer function has a variable 'message'
    
    def inner():
        nonlocal message  # This tells Python to use the 'message' in the outer function
        message = "nonlocal"  # This changes the 'message' in the outer function
        print("inner()", message)
    
    inner()  # Call the inner function to change the message
    print("outer()", message)  # Print the updated 'message' from outer

outer()  # Output will be: nonlocal

# global Keyword - makes variable global
# def myFunc():
#     global x
#     x = "hello"
#     print(x)
# myFunc()
# print(x)


# Parameters and arguments (positional, default, keyword, variable-length *args, **kwargs)

# def parameters_func(name, age):
#     print(name, age)

# parameters_func("JS", 1997)

# Default Parameters:
# def parameters_func(name="Hello", age=1000):
#     print(name, age)

# parameters_func()

#

# def parameters_func(name, age):
#     print(name, age)

# parameters_func(name="Hello", age=90)

# Variable-Length Arguments: *args and **kwargs:
# *args (Positional Variable-Length Arguments):
def nums(*nums):
    for num in nums:
        print(num)
nums(1,2,3,4,5,6)

# **kwargs (Keyword Variable-Length Arguments):
def hello(**info):
    for key, value in info.items():
        print(key, value)

hello(name="Alex", age=25, city="NYC")


# Built-In Function

# abs()
print(abs(-15))
print(abs(15.55))

# all - all should be true
numbers = [1,2,3,4,5,6]
print(all(num > 3 for num in numbers))

# any - some should be true
numbers = [1, 2, 3, 0, 4]
print(any(num > 2 for num in numbers))

# aiter() - Returns an asynchronous iterator from an asynchronous iterable.
import asyncio
# async def async_gen():
#     for i in range(3):
#         yield i
#         await asyncio.sleep(1)

# async def main():
#     async for x in aiter(async_gen()):
#         print(x)

# asyncio.run(main())

# anext()
async def async_gen2():
    yield 1
    yield 2

async def main2():
    it = aiter(async_gen2())
    print(await anext(it))
    print(await anext(it))

asyncio.run(main2())


# ascii()
print(ascii("Hello"))
print(ascii('Привет'))

# bin() - Converts an integer to a binary string.
print(bin(10))

# bool()
print(bool(0))  
print(bool(1))  