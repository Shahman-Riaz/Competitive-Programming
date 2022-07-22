(n, k) = map(int, input().split(' '))
total = 0
for lines in range(n):
    a = int(input())
    if a <= 10**9:
        if a % k == 0:
            total += 1
print(total)
