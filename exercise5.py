a = input("Please input your first words: ")

b = input("Please input your second words: ")


def swap(string1, string2):
    x = list(string1)
    y = list(string2)
    z = x.copy()
    x[:2] = y[:2]
    y[:2] = z[:2]

    c = str(x) + str(y)
    return ''.join(c)


print(swap(a, b))
