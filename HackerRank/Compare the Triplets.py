a = [6, 8, 12]
b = [7, 9, 15]
alice = 0
bob = 0
result = []
for i,j in zip(a, b):
    if (i > j):
        alice += 1
    elif (i < j):
        bob += 1
result.append(alice)
result.append(bob)
print(result)

#SOLVED