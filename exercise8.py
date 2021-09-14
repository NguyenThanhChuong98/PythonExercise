def get_longest_word(str_input):
    string = str_input.split()
    count = 0
    for x in string:
        if len(x) > count:
            count = len(x)
            word = x
    print(count)
    print(word)


get_longest_word("exercise book cat dog fish")
