from math import floor


for i in range(int(input())):
    x, y, n, r = map(int, input().split())
    lux_burg = floor(r/y)
    norm_burg = floor(r/x)
    extra_moneyAfterLux = r - (lux_burg*y)
    extra_moneyAfterNorm = r - (norm_burg*y)
    norm_burgAfterLux = floor(extra_moneyAfterLux / x)
    lux_burgAfterNorm = floor(extra_moneyAfterNorm / y)
    if (lux_burg >= n):
        print(f'0 {n}')
    elif (lux_burg < n):
        if(extra_moneyAfterLux >= x):
            if(norm_burg + lux_burg == n):
                print(f'{norm_burg} {lux_burg}')
    elif (norm_burg >= n):
        print(f'{norm_burg} 0')
    elif((r < x) or (r < y)):
            print(-1)

#NOT SOLVED Thinking