x = []
y = 0
(a, b, c, d) = map(int, input().split(' '))
x.extend((a, b, c, d))
for i in x:
    if i >= 10:
        y += 1
print(y)

# SOLVED