from math import floor
for i in range(int(input())):
    a = int(input())

    if a <= 10:
        print(a)
    elif ((floor(a/100)) + (a % 100)) <= 10:
        print((floor(a/100)) + (a % 100))
    else:
        print(-1)

#SOLVED
