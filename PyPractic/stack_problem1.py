brackets = input()
stack_brackets = []
result = True
for char in brackets:
    if char == "{" or char == "[" or char == "(":
        stack_brackets.append(*char)
    else:
        if (len(stack_brackets) > 0) and ((char == '}' and stack_brackets[-1] == '{') or (char == ']' and stack_brackets[-1] == '[') or (char == ')' and stack_brackets[-1] == "(")):
            stack_brackets.pop()
        else:
            result = False
            break

if result and len(stack_brackets) == 0:
    print("yes")
else:
    print("no")




