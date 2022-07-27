# from typing import DefaultDict

print("Hello World")

def getTax(base, rate):
    return base * rate

y = getTax(45.90, 0.05)

print(y)

x = 0
while x < 4:
    x += 1
    print(x)

pairs = {
    "sally" : 5,
    "harry" : 10
}

print ("Tax is:", getTax(25.13, 0.08))
print(pairs)

key = "sally"
print(pairs.get(key))

set2 = pairs.copy()

print(set2.get(key))
