text = input()
dict = {}

for t in text:
    dict[t] = text.count(t)

print(dict)