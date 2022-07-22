for i in range(int(input())):
    (a, b) = map(int, input().split(' '))
    print('<') if (b>a) else print('>') if (a>b) else print('=')