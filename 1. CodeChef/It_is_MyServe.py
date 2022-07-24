n = int(input())
for i in range(n):
    (a, b) = map(int, input().split(' '))
    print('Alice') if (a > b or a == b) else print('Bob')