def change_word(string):
    not_word = string.find("not")
    poor_word = string.find("poor")
    if poor_word > not_word and poor_word > 0 and not_word > 0:
        result = string.replace(string[not_word:(poor_word + 4)], "good")
        return result
    else:
        return string


print(change_word("the lyrics is not that poor"))

