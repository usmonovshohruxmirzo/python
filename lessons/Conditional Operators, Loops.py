# The Boolean Type

# On/Off
# Yes/No
# True/False
# 1/0

# Text and numerical values can have a Boolean context, which causes expressions to be classified as truthy or falsy. For different programming languages, the standards for determining an expression's Boolean value change.

print(0 == False)
print(1 == True)
print(5 == 1)
print(5 == 0)
print(5 == True)
print(5 == False)

# Conditional Operators and Conditional Statements

# The main use cases of if-else statements in Python include:
#
# `Conditional` execution: executing different blocks of code based on whether a condition evaluates to true or false
# `Error handling`: handling errors or exceptional cases by providing alternative paths of execution
# `Input validation`: validating user input and responding accordingly based on the validity of the input
# `Loop control`: controlling the flow of loops by including if-else statements within loop constructs
# `Decision-making`: making decisions within a program based on specific conditions, such as branching logic in algorithms or control flow in applications
# `User interaction`: creating interactive programs where the user's input determines the program's behavior
# `Data filtering`: filtering data based on specific criteria, such as selecting items from a list that meet certain conditions
# `Configuration management`: configuring program settings or behavior dynamically based on certain conditions or environment variables

condition = True
if condition:
    # Executes when the condition is true
    print("IF")
else:
    # Executes when the condition is false
    print("ELSE")

x = 10
if x > 5: print(True)
else: print(False)

operation = "read"
if operation == "read":
    print("perform read operation…")
elif operation == "update":
    print("perform update operation …")
elif operation == "insert":
    print("perform insert operation …")
elif operation == "delete":
    print ("perform delete operation …")
else:
    print("wrong variant if operation !!! ")

# Advanced Techniques for Complex Decision-Making Structures
# Nested If statement
x = 10
if x > 5:
    print("x is greater than 5")
    if x == 10: print("x is equal to 10")
else: print("x is less than or equal to 5")

# match/case
number = 1
match number:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case _: print("not found")  # case _ == `default` in JS

# ternary operator
name = "alex"
result = "alex" if name == "alex" else "Wrong Name"
print(result)

num = 15
num_2 = 2
num_result = f"correct, {num} is greater than {num_2}" if num > num_2 else f"wrong, {num} is less than {num_2}"
print(num_result)


# Loops
# The while Loop - The loop runs while the condition expression is true.
# x = int(input("Please input 0 to stop iteration: "))
# sum_result = 0
# while x:
#     sum_result  += x
#     x = int(input("Please input 0 to stop iteration: "))
# print(sum_result)


# continue
# n = int(input("Input integer number: "))
# sum_result = 0
# x = 1
#
# while x < n:
#     x += 1
#     if x % 2:
#         continue
#     sum_result += x
# print(print(f"Sum of even numbers: {sum_result}"))

# break
# x = int(input("Imput integer number: "))
# is_prime = True
# div = 2
#
# while div < x:
#     if not x % div:
#         is_prime = False
#         break
#     div += 1
# if is_prime:
#     print("Prime")
# else: print("Not prime")


# else
# x = 1
# while x < 5:
#     print(x)
#     x += 1
# else: print(f"Loop was stopped at: {x}")

# The for Loop

# for i in range(0, 10, 2):
#     print(i)

# words = ['cat', 'window', 'defenestrate']
# for word in words:
#     print(word, len(word))

# num = int(input("enter num"))
# for i in range(10):
#     if num == i:
#         for a in range(10):
#             print(f"{i} * {a} = {i * a}")


# Solving Problems
# Example 1: Number Analysis
# numbers_input = input("Enter a series of numbers separated by spaces: ")
# numbers_list = []
# even_count = 0
# odd_count = 0
# for num in range(int(numbers_input)):
#     numbers_list.append(num)
#     if num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print("Count of even numbers:", even_count)
# print("Count of odd numbers:", odd_count)
# print(numbers_list)


# Example 2: Guessing Game
import random

secret_number = random.randint(1, 100)
guess_count = 0
print("Welcome to the Guessing Game!")
print("I have selected a number between 1 and 100. Can you guess it?")
while True:
    guess = int(input("Enter your guess: "))
    guess_count += 1
    if guess == secret_number:
        print("🎉 Congratulations! You guessed the correct number in", guess_count, "guesses.")
        break
    elif guess > secret_number:
        print("Too high! Try guessing a lower number.")
    elif guess < secret_number:
        print("Too low! Try guessing a higher number.")
    else:
        print("try Again")