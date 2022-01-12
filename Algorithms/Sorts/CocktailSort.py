lst = [44, -2, -90, -3, 55, -999]

def cockt(array):
    sort = array[:]
    right, left = 0, 0
    for i in range(len(sort)):
        for j in range(left, len(sort) - 1 - right):
            if sort[j] > sort[j + 1]:
                sort[j], sort[j + 1] = sort[j + 1], sort[j]
        right += 1

        for n in range(1 + right, len(sort) - left):
            if sort[-n] < sort[-n - 1]:
                sort[-n], sort[-n - 1] = sort[-n - 1], sort[-n]
        left += 1
    return sort


print(cockt(lst))
