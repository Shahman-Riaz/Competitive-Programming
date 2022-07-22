for i in range(int(input())):
    grades = int(input())
    if (grades < 38):
        print(grades)
    else:
        for i in range(5, 101, 5):
            if (i>grades or i==grades):
                if ((i-grades) < 3):
                    print(i)
                    break
                elif((i-grades) >= 3 ):
                    print(grades)
                    break
                break

#Solved