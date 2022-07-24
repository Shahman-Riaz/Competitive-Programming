for i in range(int(input())):
    a, b, n = map(int, input().split())
    soln = 0
    if (a != b):
        while((soln == 0)):
            if ((n % a == 0) and (n % b != 0)):
                print(n)
                soln = n
            else:
                n += 1
    else:
        print(-1)
            