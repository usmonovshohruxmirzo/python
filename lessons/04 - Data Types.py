# Text Type: 	    str
# Numeric Types: 	int, float, complex
# Sequence Types: 	list, tuple, range
# Mapping Type: 	dict
# Set Types: 	    set, frozenset
# Boolean Type: 	bool
# Binary Types: 	bytes, bytearray, memoryview
# None Type: 	    NoneType


# You can get the data type of any object by using the `type()` function:

# x = 5
# print(x, type(x)) # int

# s = "Hello"
# print(s, type(s)) # str

# fl = 20.10
# print(fl, type(fl)) # float

# comlx = 1j # complex
# print(comlx, type(comlx))

# lst = ["apple", "banana", "cherry"]
# print(lst, type(lst)) # list

# tupl = ("apple", "banana", "cherry")
# print(tupl, type(tupl)) # tupl

# rnge = range(6)
# print(rnge, type(rnge))

# dct = {"name": "Alex", "age": 20}
# print(dct, type(dct))

# st = {"html", "css", "js"}
# print(st, type(st)) # set

# frset = frozenset({"html", "css", "js"})
# print(frset, type(frset)) # frozenset

# bl = True
# print(bl, type(bl)) # bool

# byt = b"Hello"
# print(byt, type(byt)) # bytes

# bytarr = bytearray(5)
# print(bytarr, type(bytarr)) # bytearray

# memoryvw = memoryview(bytes(5))
# print(memoryvw, type(memoryvw)) # memoryview

# n = None
# print(n, type(n)) # NoneType


# Setting the Specific Data Type
# If you want to specify the data type, you can use the following constructor functions:

xstr = str("Hello World")
print(xstr)

xnum = int(10)

xfloat = float(2.5)

xcomplex = complex(1j)
complex_number = complex("1+3j")
print(complex_number)

xlist = list(("a", "b", "c")) # ordered sequence of elements, mutable or changeable.

xtuple = tuple(("a", "b", "c")) # Python tuples are a type of data structure that is very similar to lists. The main difference between the two is that tuples are immutable

xrange = range(0, 10) # a function that returns a sequence of numbers
print(xrange)

xdict = dict(id=1, name="Alex", job="Front-End Developer", salary=3000)
print(xdict)

xset = set(("a", "b", "c", "c")) # unordered list
print(xset)

xfronzenset = frozenset(("a", "b", "c", "c")) # An immutable version of a Python set object
print(xfronzenset)

xbool = bool(5)

xbytes = bytes(5) # Python bytes() We utilize the Python bytes() method to manipulate binary data in the program. The byte is a digital information unit that typically consists of 8 bits each of which consists of a 0 or 1.

xbytearray = bytearray(5) # an array of given bytes

xmemoryview = memoryview(bytes(5)) # allows Python code to access the internal data of an object's buffer without making a copy of it. 