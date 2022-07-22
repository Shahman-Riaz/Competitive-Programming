for i in range(int(input())):
    x, y, z = map(int, input().split())

    break_num = x // 3
    extra_level = x % 3
    if(x<=3):
        print(x*y)
    elif ((x>3) and (extra_level == 0)):
        print((3 * y * break_num) + (z * (break_num - 1)) + (extra_level * y))
    elif (x>3):
        print((3 * y * break_num) + (z * break_num) + (extra_level * y))
    
        

# SOLVED