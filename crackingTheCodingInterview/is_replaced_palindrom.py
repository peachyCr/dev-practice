def is_replaced_palindrom(string):
    dict_char = {}
    for char in string:
        if char == " ":
            continue
        if char in dict_char.keys():
            dict_char[char] += 1
        else:
            dict_char[char] = 1

    lonely_char = 1
    for v in dict_char.values():
        lonely_char -= v % 2

    if lonely_char < 0:
        return False
    else:
        return True


string = input()
print(is_replaced_palindrom(string))
