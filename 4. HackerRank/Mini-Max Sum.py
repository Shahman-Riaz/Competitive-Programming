arr = [1, 2, 3, 4, 5]
min_sum = 0
max_sum = 0
arr.sort()
for i in arr[:(len(arr)-1)]:
    min_sum += i
for i in arr[-(len(arr)-1)::]:
    max_sum += i
print(min_sum , max_sum)

#SOLVED

