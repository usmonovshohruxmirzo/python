def add(a: int, b: int) -> int:
    return a + b

def division(a: int, b: int) -> tuple:
    if b == 0:
        raise ZeroDivisionError(f"Cannot divide {a} by {b} (division by zero)")
        # raise == throw in JS
    result = a / b
    return int(result), f"The result of {a} divided by {b} is {result}"

def multiplication(a: int, b: int) -> int:
    return a * b

def subtraction(a: int, b: int):
    return a - b
