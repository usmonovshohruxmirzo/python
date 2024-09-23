print(10 > 9)
print(10 == 9)

a = 200
b = 33

if a > b:
    print(f"{a} is greater than {b}")
else: 
    print(f"{b} is less than {a}")

# Most Values are True
print(bool("Hello"))
print(bool(15))
print(bool(["apple", "cherry", "banana"]))

# Some Values are False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

class myClass():
    def __len__(self):
        return 0
    
myObj = myClass()
print(bool(myObj))

def myFunc():
    return True

print(myFunc())

if myFunc():
    print("YES!")
else:
    print("NO")

x = 200
print(isinstance(x, int))