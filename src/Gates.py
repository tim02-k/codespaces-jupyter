def Not(a):
    return not a

def Or(a, b):
    return a or b

def And(a, b):
    return a and b

def Nand(a, b):
    return not (a and b)

def Nor(a, b):
    return not (a or b)

def Xor(a, b):
    return a != b

def Xnor(a, b):
    return a == b

print(Not(True))
print(Or(True, False))
print(And(True, False))
print(Nand(True, False))
print(Nor(True, False))
print(Xor(True, False))
print(Xnor(True, False))

for i in range(int(input("Number: "))): print(str(i)*i)