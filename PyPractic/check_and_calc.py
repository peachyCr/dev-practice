def delZeros(stack):
    while len(stack) > 0 and stack[-1] == ' ':
        stack.pop(-1)
    return stack

def checkIsOk(seq):
    okSymb = ['+', '*', ')', '(', '-', ' ']
    okNums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if seq[0] in ['+', '*', ')']:
        return False
    cnt_brackets = 0
    stack = []
    for i in range(len(seq)):
        if (seq[i] in okSymb or seq[i] in okNums) and cnt_brackets >= 0:
            if seq[i] == '(':
                stack = delZeros(stack)
                if len(stack) > 0:
                    if stack[-1] in okNums:
                        return False, None
                cnt_brackets += 1
            elif seq[i] == ')':
                stack = delZeros(stack)
                if len(stack) > 0:
                    if stack[-1] in ['+', '-', '*']:
                        return False, None
                cnt_brackets -= 1
            elif seq[i] in okNums:
                isZero = False
                if len(stack) > 0:
                    if stack[-1] == ' ':
                        isZero = True
                stack = delZeros(stack)
                if len(stack) > 0:
                    if (stack[-1] in okNums and isZero) or stack[-1] == ')':
                        return False, None
            elif seq[i] == '-':
                stack = delZeros(stack)
                if len(stack) > 0:
                    if stack[-1] in ['+', '-', '*']:
                        return False, None
            elif seq[i] == '+' or seq[i] == '*':
                stack = delZeros(stack)
                if len(stack) > 0:
                    if stack[-1] in ['+', '-', '*', '(']:
                        return False, None
                else:
                    return False, None

            stack.append(seq[i])
        else:
            return False, None

    stack = delZeros(stack)
    if len(stack) > 0:
        if stack[-1] not in okNums and stack[-1] != ')':
            return False, None
    if cnt_brackets != 0:
        return False, None
    return True, stack

def digitsInNums(stack):
    i = 0
    infix = []
    while i < len(stack):
        if stack[i].isdigit():
            j = i
            val = ''
            while j < len(stack) and stack[j].isdigit():
                val += stack[j]
                j += 1
            infix.append(int(val))
            i += (j - i - 1)
        else:
            if stack[i] == '-' and (i == 0 or stack[i - 1] == '('):
                infix.append(0)
            infix.append(stack[i])
        i += 1
    return infix

def infixToPostfix(infix):
    stack_infix = []
    result = []
    for elem in infix:
        if isinstance(elem, int):
            result.append(elem)
        elif elem == '(':
            stack_infix.append(elem)
        elif elem == ')':
            while stack_infix[-1] != '(':
                result.append(stack_infix[-1])
                stack_infix.pop(-1)
            stack_infix.pop(-1)
        else:
            if elem in ['+', '-']:
                if len(stack_infix) > 0:
                    while len(stack_infix) > 0 and stack_infix[-1] in ['-', '+', '*']:
                        result.append(stack_infix[-1])
                        stack_infix.pop(-1)
                stack_infix.append(elem)
            elif elem == '*':
                if len(stack_infix) > 0:
                    while len(stack_infix) > 0 and stack_infix[-1] == '*' :
                        result.append(stack_infix[-1])
                        stack_infix.pop(-1)
                stack_infix.append(elem)
    while len(stack_infix) > 0:
            result.append(stack_infix[-1])
            stack_infix.pop(-1)
    return result

def replace(stack, val):
    stack.pop(-1)
    stack.pop(-1)
    stack.append(val)
    return stack

def calcPostfix(seq):
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
    return stack


seq = input()
result, stack = checkIsOk(seq)
if len(seq) == 0 or not result:
    print("WRONG")
else:
    infix = digitsInNums(stack)
    if len(infix) == 0:
        print("WRONG")
    print("infix", infix)
    postfix = infixToPostfix(infix)
    print("postfix", postfix)
    result = calcPostfix(postfix)
    print(*result)

