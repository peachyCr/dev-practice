def str_in_str(a, b):
    if len(a) != len(b):
        print("false")
        return False
    else:
        dict_a = {}
        for char in a:
            if char in dict_a.keys():
                dict_a[char] += 1
            else:
                dict_a[char] = 1
        for char in b:
            if char in dict_a.keys():
                dict_a[char] -= 1
                if dict_a[char] == 0:
                    del dict_a[char]
            else:
                print("false!")
                return False
        print("true")
        return True

a = input()
b = input()
str_in_str(a, b)
