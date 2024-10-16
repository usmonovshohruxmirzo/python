# Python Numbers

# There are three numeric types in Python:

# int
# float
# complex


x = 1 # Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
y = 2.5 # Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
z = 3j # Complex numbers are written with a "j" as the imaginary part:

# print(x, type(x))
# print(y, type(y))
# print(z, type(z))

# Type Conversion

# print(float(x))
# print(int(y))
# print(complex(x))

# Random Number
# import random
# print(random.randrange(1, 10))


# ================= integers

# bin = 0b1010
# oct = 0o36701
# hex = 0xf6a10d

# print(bin, type(bin))
# print(oct, type(oct))
# print(hex, type(hex))

# n = 10 ** 10000
# print(n)

# import sys
# # print(sys.get_int_max_str_digits())
# sys.set_int_max_str_digits(20000)
# n = 10 ** 10000
# print(n)
#
# result1 = 1000000000000
# result2 = 1_000_000_000_000
# print(result1)
# print(result2)

# input = input("enter number: ")
# print(int(input).as_integer_ratio()) # output (10, 1) - 10/1 means. A method that returns a float as a tuple of integers representing its exact fraction form (numerator, denominator).
# print(int(input).bit_count()) # The .bit_count() method counts the number of 1 bits in the binary representation of an integer.
# print(int(input).bit_length()) # returns bit length. bit: 10100 length: 5
# print(int(input).to_bytes()) # b - bytes object. '\x14' - hexadecimal. b'\x14' is called a bytes object in Python.

# to_bytes = int(input).to_bytes()
# from_bytes = int.from_bytes(to_bytes)
# print(to_bytes, from_bytes)

# Floating point numbers
# big = 1.79e308 # e means 0
# bigger = 1.8e308
# print(big)
# print(bigger)

# small = 5.0e-324
# smaller = 1.0e-324
# print(small)
# print(smaller)

# import sys # system
# print(sys.float_info)

# input_1 = 2.0
# input_2 = 2.5
# print(input_1.as_integer_ratio())
# print(input_2.as_integer_ratio())
# print(input_1.is_integer()) # why True bcz 2.0 = 2
# print(input_2.is_integer())

# output_input_2 = input_2.hex() # The .hex() method in Python converts an integer or a bytes object to its hexadecimal string representation.
# print(output_input_2, type(output_input_2))

# result = float.fromhex(output_input_2) # The .fromhex() method in Python is used to convert a hexadecimal string back into a bytes object.
# print(result, type(result))

# sign defines whether the number is positive or negative. It may be either + or -. Only the - sign is required because + is the default.
# "0x" is the hexadecimal prefix.
# "Integer" is a string of hexadecimal digits representing the whole part of the float number.
# "." is a dot that separates the whole and fractional parts.
# "fraction" is a string of hexadecimal digits representing the fractional part of the float number.
# "p" allows an exponent value to be added.
# "exponent" is a decimal integer with an optional leading sign.

import math # used to math operation
print(math.floor(3.5))
print(math.ceil(3.5))

# ========= Complex numbers
# Complex numbers are in the form
# a + bi
# where a and b are real numbers and i is the imaginary unit.
# in Python, j or J should be used instead of i.

a = 15 + 16j
print(a, type(a))
print(a.real, a.imag)
print(a.conjugate()) # used to changing sign of a number.

i = 5
f = 6.7
c = 15 + 16j

result_1 = i + f
result_2 = i + c
result_3 = f + c

print(result_1, type(result_1))
print(result_2, type(result_2))
print(result_3, type(result_3))
