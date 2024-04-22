string = input()
num = int(input())

new_str = ""
for i in range(num):
    if string[i] == " ":
        new_str += "%20"
    else:
        new_str += string[i]
print(new_str)
