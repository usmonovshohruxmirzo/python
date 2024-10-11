# Python divides the operators in the following groups:

#     Arithmetic operators
#     Assignment operators
#     Comparison operators
#     Logical operators
#     Identity operators
#     Membership operators
#     Bitwise operators

# Python Arithmetic Operators
# print(10 + 10)
# print(10 - 5)
# print(5 * 2)
# print(10 / 2)
# print(10 % 3)
# print(2 ** 2)

# print(5 // 3)
# print(5 / 3)


#! Assignment Operators
x = 5
x += 10
x -= 5
x *= 5
# x /= 2
# x %= 2
# x //= 2
# x **= 2


# y = 5 # 5 in binary is 101
# y &= 2 # 2 in binary is 010 
# print(y)

# In the operation 101 & 010 (which are 5 and 2 in decimal):

#     Bitwise AND compares each bit:
#         1 & 0 = 0
#         0 & 1 = 0
#         1 & 0 = 0

# Since there are no positions where both bits are 1, the result is 000, which is 0 in decimal.

# So, x &= 2 sets x to 0.

# y = 5 # 5 in binary is 101
# y |= 2 # 2 in binary is 010 
# print(y)

#     Bitwise OR compares each bit:
#         1 & 0 = 1
#         0 & 1 = 1
#         1 & 0 = 1
# 111  is (7) 3-Bit Binary

y = 5 # 5 in binary is 101
y ^= 2 # 2 in binary is 010 
print(y)

# Explanation of XOR (^):

#     XOR returns 1 if the bits are different and 0 if they are the same:
#         1 XOR 0 = 1
#         0 XOR 1 = 1
#         1 XOR 1 = 0
#         0 XOR 0 = 0

# XOR vs OR
# The OR operation returns 1 if at least one of the bits is 1. It returns 0 only if both bits are 0.
# 1 & 1 = 1 
# The XOR operation returns 1 if the bits are different (i.e., one is 1 and the other is 0). It returns 0 if both bits are the same.
# 1 ^ 1 = 0

y = 5   
y <<= 2 
print(y)
# 5 * 2^2 = 5 * 4 = 20
# 20 in binary 10100

y = 10
y <<= 2
print(y)
# 10 * 2^2 = 10 * 4 = 40


# x <<= 2
# print(x)

# print(x := 2)

# Comparison Operators

# Logical Operators

# Identity Operators

# Bitwise Operators

# Operator Precedence