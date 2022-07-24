for i in range(int(input())):
    x, y, n, r = map(int, input().split())
    if(y>x and r > x and r > y):
        for i in range(n, -1, -1):
            if((((n-i)*x) + ((i)*y)) <= r):
                print(f'{n-i} {i}')
                break
        else:
            print(-1)
    else:
        print(-1)
            

#NOT SOLVED Thinking