lst = [-7, 6, 1, 15, 11, 8, 4, 1, 10, -2]


def insertion(array):
    sort = array[:]
    for i, elem in enumerate(sort):
        j = i - 1
        while elem < sort[j] and j >= 0:
            j -= 1

        if j != i - 1:
            sort.insert(j + 1, elem)
            sort.pop(i + 1)
    return sort


print(insertion(lst))

