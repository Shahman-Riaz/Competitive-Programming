def avg(nums):
    sum = 0
    for i in nums:
        sum += i
    print(f'{sum / len(nums):.2f}')

nums = list(map(int, input().split()))
avg(nums)

# SOLVED