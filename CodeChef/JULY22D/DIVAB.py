for i in range(int(input())):
    a, b, n = map(int, input().split())
    break_loop = True
    if (a != b):
        while((n <= (1e09))):
            if ((n % a == 0) and (n % b != 0)):
                print(n)
                break
            n += 1
    else:
        print(-1)
        
            