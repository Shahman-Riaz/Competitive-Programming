from math import ceil
a = int(input())
if a > 0:
    if a in range(1, 6):
        print(1)
    elif a > 5:
        print(ceil(a/5))