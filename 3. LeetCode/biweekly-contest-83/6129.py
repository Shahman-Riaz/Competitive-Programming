# nums = [1,3,0,0,2,0,0,4]
nums = [0, 0, 0, 2, 0, 0]
zero_num = nums.count(0)
result = 0
if (zero_num > 0):
    for i in range(zero_num, 0, -2):
        result += i
    print(result)
else:
    print(0)
    

