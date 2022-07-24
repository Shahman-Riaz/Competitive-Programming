for i in range(int(input())):
    n = int(input())
    s = str(input())
    s_count = s.count('START38')
    l_count = s.count('LTIME108')
    if(n == (s_count + l_count)):
        print(f' {s_count} {l_count}')

#SOLVED