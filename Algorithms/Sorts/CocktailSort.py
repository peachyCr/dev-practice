lst = [1, 15, 22, 0, 10, -1, 90, -12]

def cockt(array):
    sort = array[:]
    right, left = 0, 0
    for i in range(len(sort) - 1):
        for j in range(left, len(sort) - 1 - right):
            if sort[j] > sort[j + 1]:
                sort[j], sort[j + 1] = sort[j + 1], sort[j]
        right += 1

        for n in range(1 + right, len(sort) - left):
            if sort[-n] < sort[-n - 1]:
                sort[-n], sort[-n - 1] = sort[-n - 1], sort[-n]
        left += 1
    return sort


print(coct(lst))
