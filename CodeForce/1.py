(a, b, c, d, e) = map(int, input().split(' '))
arr = [a, b, c, d, e]
dup_arr = []
for i in arr:
    if arr.count(i) == 2:
        dup_arr.append(i)
    # elif i not in dup_arr:
    #     dup_arr.append(i)
print(dup_arr)