for i in range(int(input())):
    (a, b, c, d) = map(int, input().split(' '))
    num =[b, c, d]
    sum = 0
    for i in num:
        if i > a:
            sum += 1
    print(sum)