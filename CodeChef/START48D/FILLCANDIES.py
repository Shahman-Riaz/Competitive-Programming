from math import ceil


for i in range(int(input())):
    n, k, m = map(int, input().split())
    print(ceil(n/(k*m)))
