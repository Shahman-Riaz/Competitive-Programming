for d in range(int(input())):
    n = int(input())
    s = list(input().upper())
    y = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
    }
    text = ''
    x = ['A', 'T', 'G', 'C']
    if (n == len(s)):
        for i in s:
            if (i in x):
                text += y[i]
        print(text)

#SOLVED