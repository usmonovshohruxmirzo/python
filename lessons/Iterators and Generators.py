#  Iterators
"""
Iterator: You manually create the sequence-handling logic using __iter__ and __next__.
"""
class Counter:
    def __init__(self, start, end):
        # Initialize the counter with a start and end value
        self.current = start  # The starting value of the counter
        self.end = end        # The ending value of the counter

    def __iter__(self):
        # The __iter__ method makes this class an iterable
        # Returns the iterator object itself (self)
        return self

    def __next__(self):
        # The __next__ method provides the next value in the iteration
        if self.current > self.end:
            # If the current value exceeds the end, stop the iteration
            raise StopIteration
        value = self.current  # Save the current value to return
        self.current += 1     # Move to the next value
        return value          # Return the saved value

# Create an instance of Counter with a range from 1 to 3
counter = Counter(1, 3)

# Use a for loop to iterate over the counter object
for num in counter:
    print(num)  
    # The for loop calls __iter__() and __next__() automatically
    # Output: 1, 2, 3


class EvenNumbers:
    def __init__(self, start, end):
        self.current = start  
        self.end = end        

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.end:  # Ensure the current number is within the range
            if self.current % 2 == 0:    # Check if the current number is even
                value = self.current     # Save the even value
                self.current += 1        # Move to the next number
                return value             # Return the even number
            self.current += 1            # Skip odd numbers
        raise StopIteration              # Stop when the range is exhausted


print("evens:")
evens = EvenNumbers(3, 10)
for even in evens:
    print(even)

# Generators
"""
Generator: You use yield to automatically create an iterator in a simpler way.
"""

# def counter(start, end):
#     while start <= end:
#         yield start
#         start += 1

# for num in counter(1, 3):
#     print(num)