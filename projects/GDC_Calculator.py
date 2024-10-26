def gdc(a, b):
    while b:
        a, b = b, a % b
    return a

print(gdc(100,150))