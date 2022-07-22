name = str(input()).lower()
dist_char = []
if name != '' and len(name) <= 100:
    for i in name:
        if i not in dist_char:
            dist_char.append(i)
    print('CHAT WITH HER!') if len(dist_char) % 2 == 0 else print('IGNORE HIM!')
