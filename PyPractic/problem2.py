N, K = [int(elem) for elem in input().split()]
cars_nums = [int(i) for i in input().split()]

def cnt_prefixsum(cars_nums):
    sum_now = 0
    prefixsumbyvalue_dict = {0 : 1}
    for car in cars_nums:
        sum_now = car + sum_now
        if sum_now not in prefixsumbyvalue_dict:
            prefixsumbyvalue_dict[sum_now] = 0
        prefixsumbyvalue_dict[sum_now] += 1
    return prefixsumbyvalue_dict

def cnt_rangecars(prefixsumbyvalue_dict, K):
    cnt_ranges = 0
    for num, cnt in prefixsumbyvalue_dict.items():
        if num - K in prefixsumbyvalue_dict:
            cnt_ranges += prefixsumbyvalue_dict[num - K] * cnt
    return cnt_ranges


prefix_sum_dict = cnt_prefixsum(cars_nums)
print(prefix_sum_dict) #получили количество префиксных значений
res = cnt_rangecars(prefix_sum_dict, K)
print(res)


# 1 2 3 4 1
# 0 1 3 6 10 11

