x = -121
if x >= 0:
    a = str(x)
    b = a[::-1]
    c = int(b)
    if x == c:
        print ('true')
    else:
        print ('false')
else:
    print ('false')