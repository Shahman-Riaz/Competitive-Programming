arr = [-4, 3, -9, 0, 4, 1]
len_arr = len(arr)
len_positive, len_negative, len_zero = 0, 0, 0

for i in arr:
    if i == 0:
        len_zero += 1
    elif i < 0:
        len_negative += 1
    else:
        len_positive +=1
print(f"{len_positive/len_arr:.{len_arr}f}")
print(f"{len_negative/len_arr:.{len_arr}f}")
print(f"{len_zero/len_arr:.{len_arr}f}")

#SOLVED BUT GAVE ME SO MANY PAIN