a = str(input())
upper_num = 0
for i in a:
    if i.isupper() :
        upper_num += 1
lower_num = len(a)-upper_num
print(a.lower()) if (upper_num <= lower_num) else print(a.upper())
    
