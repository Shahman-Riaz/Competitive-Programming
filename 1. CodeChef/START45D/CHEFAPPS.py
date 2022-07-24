for i in range(int(input())):
    (a, b, c, d) = map(int, input().split(' '))
    if ((a - (b + c)) >= d):
        print(0)
    elif ((a == (b + c)) and b < d and c < d):
        print(2)
    elif ((a == (b + c)) and ((b > d or c > d) or (b > d and c > d))):
        print(1)
    elif ((a - b - c) < d and ((a - b >= d) or (a - c >= d))):
        print(1)