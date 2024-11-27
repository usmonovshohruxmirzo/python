#  Iterators
"""
Iterator: You manually create the sequence-handling logic using __iter__ and __next__.
"""
class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value
    
counter = Counter(1, 3)
for num in counter:
    print(num)  # Output: 1, 2, 3


# Generators
"""
Generator: You use yield to automatically create an iterator in a simpler way.
"""

def counter(start, end):
    while start <= end:
        yield start
        start += 1

for num in counter(1, 3):
    print(num)