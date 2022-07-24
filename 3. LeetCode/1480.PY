nums = [3, 1, 2, 10, 1]
ans = []
for i in range(len(nums)):
    if i == 0:
        ans.append(nums[i])
    if i > 0:
        ans.append(nums[i]+ans[i-1])
print(ans)

#SOLVED