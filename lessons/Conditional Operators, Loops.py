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