for i in range(int(input())):
    (a, b, c, d) = map(int , input().split(' '))
    if (a == c or b == d):
        print(2)
    elif ( a != c and b != d):
        print(1)

#SOLVED