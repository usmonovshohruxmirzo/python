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


# ============================= Comparison Operators

print(10 == 10)
print(10 == "10")
print("10" == "10")
print(10 != "10")
print(10 > 5)
print(10 < 5)
print(10 <= 5)
print(10 >= 10)


# ============================= Logical Operators

# e = 20
# r = 15
#
# print(e > 10 and r > 10) # and: &&
# print(e > 10 or r > 50) # or: ||
# print(not (e > 50 and r > 50)) # not: !


# ============================= Identity Operators

# p = 8
# q = 8
# print(p is q)
# print(p is not q)

# ============================= Operator Precedence

"""
Operator precedence determines the order in which operators are evaluated in expressions. Operators with higher precedence are evaluated before those with lower precedence.
"""

"""
1. **Parentheses `()`**
   - Highest precedence: expressions inside parentheses are evaluated first.

2. **Exponents `**`**
   - Right-to-left: `2 ** 3 ** 2` is evaluated as `2 ** (3 ** 2)`.

3. **Unary operators `+`, `-`, `~`**
   - These include positive, negative, and bitwise NOT.

4. **Multiplication `*`, Division `/`, Floor Division `//`, Modulus `%`**
   - Evaluated left to right.

5. **Addition `+`, Subtraction `-`**
   - Also left to right.

6. **Bitwise Shift `<<`, `>>`**

7. **Bitwise AND `&`**

8. **Bitwise XOR `^`**

9. **Bitwise OR `|`**

10. **Comparison `==`, `!=`, `<`, `>`, `<=`, `>=`**

11. **Logical AND `and`**

12. **Logical OR `or`**

13. **Assignment `=`, `+=`, `-=`, `*=`, `/=`, etc.**
   - Lowest precedence.
"""

# ============================= Bitwise Operators
# === Bitwise AND &
# o = 0b011 # 011 -> 3
# s = 0b111 # 111 -> 7
#
# # 0 & 1 = 0
# # 1 & 1 = 1
# # 1 & 1 = 1
# # 011 -> 3
#
# print(o & s) # 3

# === Bitwise OR &
# o = 0b011 # 011 -> 3
# s = 0b111 # 111 -> 7
#
# # 0 | 1 = 1
# # 1 | 1 = 1
# # 1 | 1 = 1
# # 111 -> 7
#
# print(o | s) # 7

# === Bitwise XOR ^
# o = 0b011 # 011 -> 3
# s = 0b111 # 111 -> 7
#
# # 0 ^ 1 = 1
# # 1 ^ 1 = 0
# # 1 ^ 1 = 0
# # 100 -> 4
#
# print(o ^ s)

# === Bitwise NOT ~ inverting bits 1 to 0, 0 to 1
# In two's complement, ~n = -(n + 1) for any integer n.
# ~3 = -(3 + 1) = -4
o = 0b011 # 011 -> 3
s = ~o # 0b100 -> -4
print(s, bin(s))

# === Bitwise left shift <<
# a = 0b011
# print(bin(a))
# a = a << 5 #  shift left by pushing zeros in from the right and letting the leftmost bits fall off
# print(bin(a))

# === Bitwise right shift >>
# a = 0b011010
# print(bin(a))
# a = a >> 2 # Shift all bits two places to the right. 10 falls off
# print(bin(a))




# walrus operator
# x = 40
# x <<= 2
# print(x := 2)



a = 19
a %= 4
print(a)

class Number:
    def __init__(self,value):
        self.value = value
        
a = Number(17)
b = Number(17)
print(a is b)

# pass is a do-nothing statement in Python. It’s used as a placeholder in empty functions, classes, or loops to avoid errors.

def my_function():
    pass  # Function does nothing for now