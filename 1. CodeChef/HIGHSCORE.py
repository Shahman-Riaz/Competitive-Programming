for i in range(int(input())):
    num = int(input())
    (a, b, c, d) = map(int, input().split(' '))
    max = 0
    if (a + b + c + d) == num:
        arr = [a, b, c, d]
        for i in arr:
            if i > max:
                max = i
        print (max)

# #SOLVED


