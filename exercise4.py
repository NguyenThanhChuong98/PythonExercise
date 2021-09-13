a = input("Please input your words: ")

b = str(a)
c = a[:]

for x in a[0:]:
    if x == a[0]:
        a[0:] = 0
    else:
        continue

print(b)

