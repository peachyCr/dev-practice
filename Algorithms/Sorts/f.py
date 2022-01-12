# n = int(input())
# A = input().split( )
# dict = {}


def kek(n, A):
    dict = {}
    if n < 3:
        return -1
    else:
        for elem in A:
            if elem in dict.keys():
                dict[elem] = dict[elem] + 1
            else:
                dict[elem] = 1

        max_val = max(dict.values())
        for k in dict.keys():
            if dict[k] == max_val:
                dict.pop(k)
                break

        sec_val = max(dict.values())
        if max_val == sec_val:
            return -1
        else:
            num_result = 0
            result = ''
            for k in dict.keys():
                if dict[k] == sec_val:
                    if num_result == 0:
                        result = k
                        num_result += 1
                    else:
                        result = -1
            return result


print(kek(3, [1,2,3])) # -1
print(kek(3, [1,2,2])) # 1
print(kek(5, [2,2,1,1,3])) # -1
print(kek(5, [2,2,2,2,1])) # 1
print(kek(6, [3,3,3,2,2,2])) # -1
print(kek(6, [3,3,3,2,2,1])) # 2
print(kek(10, [3,3,3,3,4,4,4,4,2,2])) #-1
# print(kek(, []))
# print(kek(, []))
# print(kek(, []))
