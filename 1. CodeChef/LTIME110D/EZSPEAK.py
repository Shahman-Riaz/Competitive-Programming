for i in range (int(input())):
    n = int(input())
    s = str(input())
    row_consonent = []
    len_cons = 0
    cons = ''
    vowel = ['a', 'e', 'i', 'o', 'u']
    if(len(s) == n):
        for j in s:
            if j not in vowel:
                cons += j
            elif j in vowel:
                row_consonent.append(cons)
                cons = ''
        row_consonent.append(cons)
        for k in row_consonent:
            if len_cons<len(k):
                len_cons = len(k)

    print('Yes') if (len_cons<4) else print('No')

#SOLVED