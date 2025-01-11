"""
def function_name(arg):
    <base case> # do not need to calculate, return predefined value
    function_name(<modified_arg>) # recursive call with changed argument
"""


def get_fib(n):
    n_fib = None

    if n < 1: print('N must be > 0')
    elif n == 1: n_fib = 0
    elif n == 2: n_fib = 1
    else:
        prev_2, prev_1 = 0, 1  # prev_2 – N-2 element, prev_1 – N-1
        for i in range(2, n):
            n_fib = prev_2 + prev_1  # calculate a next value of the Fib
            prev_2 = prev_1  # shift prev_2 and prev_1 values
            prev_1 = n_fib

    return n_fib

print(get_fib(10))


def recursion(n):
    print(n)
    if n == 1: return 1
    else: recursion(n - 1)

recursion(10)

import sys
def factorial(n):
    if n == 1:
        return 1
    else: n * factorial(n - 1)

sys.setrecursionlimit(1200)
print(factorial(10))
