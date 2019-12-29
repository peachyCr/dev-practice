lst = [1, 15, -22, 0, 10, -1]


def select(array):
    sort = array[:]
    for i in range(len(sort)):
        for j, elem in enumerate(sort):
            if elem == min(sort[i:]):
                index = j
        sort[i], sort[index] = min(sort[i:]), sort[i]
    return sort


print(select(lst))
