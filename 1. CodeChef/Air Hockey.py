# cook your dish here
for i in range(int(input())):
    (a, b) = map(int, input().split(' '))
    print(7-a) if (a > b or a == b) else print(7 - b)