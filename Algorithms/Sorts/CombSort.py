lst = [1, 15, 22, 0, 10, -1, 90, -12, -18, 100, 19]


def comb_sort(array):
    factor_umensheniya = 1.24
    un_sort = array
    step = int(len(un_sort) / factor_umensheniya)
    while step >= 1:
        for j in range(len(un_sort) - step):
            if un_sort[j] > un_sort[j + step]:
                un_sort[j], un_sort[j + step] = un_sort[j + step], un_sort[j]
        step = int(step / factor_umensheniya)
    return un_sort


print(comb_sort(lst))
