for i in range(int(input())):
    (x, a, b) = map(int, input().split(' '))
    print('Qualify') if (x <= ((a*1)+(b*2))) else print('NotQualify')

#solved