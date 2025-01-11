from collections import namedtuple, deque, Counter, OrderedDict, defaultdict, ChainMap, UserDict

# namedtuple
"""
A factory function to create tuple subclasses with named fields.
Use Case: Make tuples more readable by assigning names to elements.
"""
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p, p.x, p.y)  

# deque
"""
A list-like container with fast O(1) appends and pops from both ends.
Use Case: Efficiently implement queues or stacks.
"""
dq = deque([1, 2, 3])
dq.append(4)
print(dq)
dq.appendleft(0)
print(dq)

# Counter
"""
A dictionary subclass for counting hashable objects.
Use Case: Count occurrences of elements in a collection.
"""
counts = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
print(counts) # Output: Counter({'a': 3, 'b': 2, 'c': 1})

# OrderedDict
"""
A dictionary subclass that remembers the order entries were added (prior to Python 3.7 where dicts became ordered by default).
Use Case: Maintain insertion order explicitly.
"""
od = OrderedDict()
od["a"] = 1
od["b"] = 2
print(od)

# defaultdict
dd = defaultdict(int)
dd["a"] += 1
print(dd["a"], dd["b"], dd["c"])

# ChainMap
"""
Groups multiple dictionaries into a single view.
Use Case: Manage multiple scopes or namespaces.
"""
a = {"x": 1}
b = {"y": 2}
cm = ChainMap(a, b)
print(cm["x"], cm["y"])

# UserDict, UserList, UserString
"""
Wrappers around built-in types for easier subclassing.
Use Case: Customize dictionary, list, or string behavior.
"""
class MyDict(UserDict):
    def __setitem__(self, key, item):
        return super().__setitem__(key.upper(), item)
md = MyDict()
md["key"] = "value"
print(md)