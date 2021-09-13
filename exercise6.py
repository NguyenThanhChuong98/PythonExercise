a = input("Please input your words: ")

b = "ing"

c = "ly"


def add(string):
    x = str(string)
    if len(x) < 3:
        print(x)
    elif b in x:
        y = x + c
        print(y)
    else:
        z = x + b
        print(z)
    return None

print(add(a))
