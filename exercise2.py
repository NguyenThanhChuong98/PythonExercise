a = input("Please input your words: ")


def count_numb_of_char(string):
    b = dict()
    c = string
    for x in c:
        d = c.count(x)
        b[x] = d
    print(b)


count_numb_of_char(a)
