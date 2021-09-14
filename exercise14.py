# Write a Python program that accepts a comma separated
# sequence of words as input and prints the unique words
# in sorted form (alphanumerically).
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white,red

def sorted_form(str):
    set_words = set(str)
    list_words = list(set_words)
    list_words.sort()
    print(",".join(list_words))


sorted_form(["red", "white", "black", "red", "green", "black"])
