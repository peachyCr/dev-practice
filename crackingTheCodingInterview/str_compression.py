def str_compression(string):
    new_str_list = []
    i = cnt = 1
    prev_char = string[0]
    while i < len(string):
        if string[i] == prev_char:
            cnt += 1
        else:
            new_str_list.append(prev_char)
            new_str_list.append(str(cnt))
            cnt = 1
            prev_char = string[i]
        i += 1
    new_str_list.append(prev_char)
    new_str_list.append(str(cnt))
    return new_str_list

string = input()
if len(string) > 0:
    new_str_list = str_compression(string)
    if len(new_str_list) >= len(string):
        print(string)
    else:
        print(''.join(new_str_list))
else:
    print("No answer")
