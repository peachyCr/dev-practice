n = int(input())
seq = [int(elem) for elem in input().split()]
stack = []
result = []
for i in range(n):
    while len(stack) > 0 and seq[i] < stack[-1][1]:
        result.append([stack[-1][0], i])
        stack.pop(-1)
    stack.append([i, seq[i]])

if len(stack) > 0:
    for i, elem in stack:
        result.insert(i, [i, -1])

res_list = [-2] * n
for elem in result:
    ind, val = elem
    res_list[ind] = val
print(*res_list)

