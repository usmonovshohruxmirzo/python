def my_decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()  # Call the original function
        print("After calling the function.")
    return wrapper

@my_decorator
def say_hello():
    print("hello!")

say_hello()