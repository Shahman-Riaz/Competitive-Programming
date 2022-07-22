for i in range(int(input())):
    s = str(input())
    a = ''
    b = ''
    for i in range(0, len(s), 2):
        a += s[i]
    for i in range(1, len(s), 2):
        b += s[i]
    print(f'{a} {b}')

#SOLVED