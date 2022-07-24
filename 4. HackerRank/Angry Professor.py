n = 4
k = 2
a = [0, -1, 2, 1]
present_student = 0
for i in a:
    if i <= 0:
        present_student +=1
print('YES') if(k > present_student) else print('NO')

#Solved