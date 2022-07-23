nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
result = []
if (len(nums1) == m+n):
    nums1.extend(nums2)
    nums1.sort()
    for i in nums1:
        if (i != 0):
            result.append(i)
    print(result)
