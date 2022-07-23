head = [4, 1, 1, 2, 3 , 3]
no_dup = []
for i in head:
    if(i not in no_dup):
        no_dup.append(i)
no_dup.sort()
print(no_dup)
