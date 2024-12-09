n, k = [int(item) for item in input().split()]
business = [int(item) for item in input().split()]
sort_business = sorted(business)

def make_dict(business):
    dict_business = {}
    for i in range(len(business)):
        if business[i] not in dict_business:
            dict_business[business[i]] = 0
        dict_business[business[i]] += 1
    return dict_business

def cnt_days(k, dict_business):
    days = 0
    temp_dict = {}
    if n == 1:
        return 1
    for num, cnt in dict_business.items():
        cnt_to_distrib = cnt
        if not temp_dict:
            temp_dict[num] = cnt
        else:
            for t_num in temp_dict:
                if num - t_num > k and temp_dict[t_num] != 0:
                    if cnt_to_distrib >= temp_dict[t_num]:
                        temp_dict[t_num] = 0
                        cnt_to_distrib -= temp_dict[t_num]
                    else:
                        temp_dict[t_num] -= cnt_to_distrib
                        cnt_to_distrib = 0
            temp_dict[num] = cnt
    for v in temp_dict.values():
        days += v
    return days


dict_business = make_dict(sort_business)
print(cnt_days(k, dict_business))
