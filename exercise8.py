a = input("Please input your words: ")


def get_the_longest_word(string):
    b = string
    c = b.split()
    count = 0
    for x in c:
        if len(x) > count:
            count = len(x)
            word = x
    print("the longest word is " + word)


get_the_longest_word(a)
