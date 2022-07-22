for i in range(int(input())):
    a,b,c,d = map(int, input().split())
    x = a  + b
    y = c  + d
    print(y) if (x>y or x==y) else print(x)
    
#SOLVED