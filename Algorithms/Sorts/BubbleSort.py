lst = [1, 15, 22, 0, 10, -1]


def bubble_sort(lst):
    sort = lst[:]
    for i in range(len(sort) - 1):
        for j in range(len(sort) - 1 - i):
            if sort[j] > sort[j + 1]:
                sort[j], sort[j + 1] = sort[j + 1], sort[j]
    return sort


print(bubble_sort(lst))
