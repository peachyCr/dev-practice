n = int(input())
nums = [int(item) for item in input().split()]
sort_nums = sorted(nums)

def medians(nums, n):
    if n == 1:
        return nums
    first = n // 2 - 1
    last = n // 2
    result = n * [0]
    cnt = 0
    for i in range(n):
        if (n - cnt) % 2 == 0:
            if nums[first] <= nums[last]:
                result[i] = nums[first]
                first -= 1
        else:
            result[i] = nums[last]
            last += 1
        cnt += 1
    return result


print(*medians(sort_nums, n))