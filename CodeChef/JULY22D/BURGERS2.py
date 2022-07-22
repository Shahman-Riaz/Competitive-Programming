from math import floor


for i in range(int(input())):
    x, y, n, r = map(int, input().split())
    prim_burg = floor(r/y)
    extra_money = r - (prim_burg*y)
    norm_burg = floor(extra_money / x)
    if (prim_burg + norm_burg == n):
        print(prim_burg + norm_burg)
    else:
        print('-1')

#NOT SOLVED Thinking