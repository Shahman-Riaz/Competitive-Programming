n = int(input())
a = [int(x) for x in str(n)]
text =''
for i in a:
    if (i == 4) or (i == 7):
        if(a.count(4)>0 and a.count(7)>0):
            text = 'YES'
        else:
            text='NO'
            break
    else:
        text = 'NO'
        break
print(text)
