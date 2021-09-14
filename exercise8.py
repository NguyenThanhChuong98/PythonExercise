def get_longest_word(str_input):
    list_words = []
    for x in str_input:
        list_words.append((len(x), x))
    list_words.sort()
    print(list_words)
    biggest_word = list_words[-1]
    print(biggest_word[1])
    print(biggest_word[0])


data = ["exercise", "book", "cat", "dog", "fish"]
get_longest_word(data)
