for i in range(int(input())):
    x = str(input())
    if(len(x) > 10):
        print(f'{x[0]}{len(x)-2}{x[-1]}')
    elif(0 < len(x) <= 10):
        print(x)
#SOLVED 