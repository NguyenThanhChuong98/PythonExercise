a = input("Please input your words:")


def remove_index_char(str, n):
    x = list(str)
    y = x[n]
    print(y)
    x.remove(y)
    print(x)


remove_index_char(a, 2)
