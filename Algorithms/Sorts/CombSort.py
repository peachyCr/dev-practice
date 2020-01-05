lst = [1, 15, 22, 0, 10, -1, 90, -12, -18, 100, 19]

def comb_sort(array):
    factor_umensheniya = 1.24
    un_sort = array
    step = round(len(un_sort) / factor_umensheniya)
    while step >= 1:
        for i in range(len(un_sort)):
            for j in range(len(un_sort) - step):
                if un_sort[j] > un_sort[j + step]:
                    un_sort[j], un_sort[j + step] = un_sort[j + step], un_sort[j]
                    print("massiv",un_sort)
        if step == 2 or 1:
            step -= 1
        step = round(step / factor_umensheniya)
    return un_sort


print(comb_sort(lst))
