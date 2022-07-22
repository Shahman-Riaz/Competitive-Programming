arr = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]
left_right = 0
right_left = 0
arr_2 = arr[::-1]

for i in range(len(arr)):
    left_right += arr[i][i]
for j in range(len(arr)):
    right_left += arr_2[j][j]

print(abs(left_right-right_left))


#SOLVED