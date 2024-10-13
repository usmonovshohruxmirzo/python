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


# integers

bin = 0b1010
oct = 0o36701
hex = 0xf6a10d

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
# print(int(input).as_integer_ratio())
# print(int(input).bit_count())
# print(int(input).bit_length())
# print(int(input).to_bytes())
#
# output1 = int(input).to_bytes()
# output2 = int.from_bytes(output1)
# print(output2, type(output2)