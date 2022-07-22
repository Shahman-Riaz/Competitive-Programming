for i in range(int(input())):
    a, b = map(int, input().split())
    text = ''
    if (a == 0 or a % 2 == 0):
        text = 'noChange'
    elif(a % 2 != 0):
        text = 'change'

    if (b == 0 and text == 'change'):
        print('On')
    elif(b == 1 and text == 'Change'):
        print('Off')
    elif (b == 0 and text == 'noChange'):
        print('Off')
    elif(b == 1 and text == 'noChange'):
        print('On')