n, k = [int(elem) for elem in input().split()]
seq = [int(elem) for elem in input().split()]

result = []
stack = []
for i in range(k):
    a = min(seq[i:i + k])
    stack.append(a)

i = k - 1
while i + k <= n:
    print(stack)
    if len(stack) > 0 and stack[-1] > seq[i + k - 1]:
        stack.pop(-1)
        stack.append(seq[i])
    result.append(stack[-1])
    i += 1
print(result)
