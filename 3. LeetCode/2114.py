sentences = ["please wait", "continue to fight", "continue to win"]
x = 0
for i in sentences:
    if i.count(' ') > x:
       x = i.count(' ')  
print(x + 1)

#SOLVED