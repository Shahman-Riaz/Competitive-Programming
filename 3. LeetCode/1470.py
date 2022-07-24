nums = [2,5,1,3,4,7,9]
n = int(len(nums)/2)
num1 = nums[:n]
num2 = nums[n:]
print(num2)
pums =[]
if int(len(nums)/2) == n and int(len(nums) % 2) == 0:
    for i, j in zip(num1, num2):
        pums.append(i)
        pums.append(j)
print(pums)


#SOLVED