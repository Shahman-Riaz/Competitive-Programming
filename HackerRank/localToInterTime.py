s = input()
if 'PM' in s:
    if s[0:2] == '12':
        print(s[0:2] + s[2:-2])
    else:
        print(str(int(s[0:2]) + 12) + s[2:-2])

elif 'AM' in s:
    if s[0:2] == '12':
        print('00' + s[2:-2])
    else:
        print(s[0:2] + s[2:-2])