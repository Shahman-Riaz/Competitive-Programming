nums = [10, 2, 7]
y = ''.join(map(str, nums))
z = ''.join(sorted(y, reverse=True))
print(z)