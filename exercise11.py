def remove_odd(str):
    new_str = ""
    for x in range(len(str)):
        if x % 2 == 0:
            new_str = new_str + str[x]
    return new_str


print(remove_odd("abcdefgh"))
