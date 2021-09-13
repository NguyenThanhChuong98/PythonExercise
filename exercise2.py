a = input("Please input your words: ")

b = dict()

for x in a:
    c = a.count(x)
    b[x] = c

print(b)
