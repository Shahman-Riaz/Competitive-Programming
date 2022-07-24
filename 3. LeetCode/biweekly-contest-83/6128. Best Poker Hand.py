# ranks = [13,2,3,1,9]
# suits = ["a","a","a","a","b"]

# ranks = [4,4,2,4,4]
# suits = ["d","a","a","b","c"]

ranks = [10,10,2,12,9]
suits = ["a","b","c","a","d"]

result = ''
cards = 0

if(len(ranks)== len(suits)):
    for i, j in zip(ranks, suits):
        if(i not in suits):
            for k in ((range(len(ranks)-1))):
                if ((ranks[k] == ranks[k+1]) or (suits[k] == suits[k+1])):
                    result = 'Flush'
                # elif ((ranks[k] != ranks[k+1]) or (suits[k] != suits[k+1])):
                #     result = 'High'
            if ((ranks.count(i) >= 3) or (suits.count(j) >= 3)):
                result = 'Three of a Kind'
            if ((ranks.count(i) == 2) or (suits.count(j) == 2)):
                result = 'Pair'
            # else:
            #     result ='High'
    print(result)


    
#     nums = [1,3,0,0,2,0,0,4]
# # zero_num = nums.count(0)
# # print(zero_num)
# no_dup = []

# for i in nums:
#     if i not in no_dup:
#         no_dup.append(i)
#         print(nums.count(i))