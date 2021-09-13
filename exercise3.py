a = input("Please input your words: ")

b = a[:2]

c = a[-2:]

if len(a) < 2:
    print("Empty String")
else:
    print(str(b) + str(c))
