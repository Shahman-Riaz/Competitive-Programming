for i in range(int(input())):
    n, k, x, y = map(int, input().split())
    if (n == k):
        print(k*x)
    elif(k < n):
        print((n-k))
#SOLVED