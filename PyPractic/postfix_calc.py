def replace(stack, val):
    stack.pop(-1)
    stack.pop(-1)
    stack.append(val)
    return stack

seq = [str(char) for char in input().split()]
stack = []
for char in seq:
    if char == '-':
        new_value = stack[-2] - stack[-1]
        replace(stack, new_value)
    elif char == '+':
        new_value = stack[-1] + stack[-2]
        replace(stack, new_value)
    elif char == '*':
        new_value = stack[-1] * stack[-2]
        replace(stack, new_value)
    else:
        stack.append(int(char))
print(*stack)
