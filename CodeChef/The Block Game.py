for i in range(int(input())):
    a = int(input())
    b = str(a)
    c = b[::-1]
    print('wins') if (b == c) else print('loses')

