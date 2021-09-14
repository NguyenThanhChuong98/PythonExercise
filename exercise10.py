def swap(str):
    first_element = str[0]
    last_element = str[-1]
    body_part = str[1:-1]
    new_str = last_element + body_part + first_element
    return new_str


print(swap("london"))
