n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

if n == len(arr):
    arr2 = arr[::-1]
    for i in arr2:
        print(i, end=" ")
