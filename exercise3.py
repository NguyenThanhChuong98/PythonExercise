a = input("Please input your words: ")


def get_two_first_and_last_char(string):
    x = string
    b = x[:2]
    c = x[-2:]
    if len(x) < 2:
        print("Empty String")
    else:
        print(b + c)


get_two_first_and_last_char(a)
