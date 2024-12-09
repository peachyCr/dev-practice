def get_prefix_sum(n, nums_list):
    prefix_sum = (n + 1) * [0]
    prefix_sum[0] = 0
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + nums_list[i - 1]
    return prefix_sum[1:]

n = int(input())
nums_list = [int(i) for i in input().split()]
result = get_prefix_sum(n, nums_list)
print(*result)

