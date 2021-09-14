a = input("Please input your words:")


def remove_index_char(str, n):
    x = str
    y = x[n]
    z = x.replace(y,'')
    print(z)




remove_index_char(a, 2)
