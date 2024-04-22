str1 = input()
str2 = input()

if str1 == str2:
    print("True")
if len(str1) > len(str2):
    min_str = str2
else:
    min_str = str1

diff_str = abs(len(str1) - len(str2))
i = cnt_not_equil = 0
while i < len(min_str):
    if str1[i] != str2[i]:
        cnt_not_equil += 1
    i += 1

if (cnt_not_equil == 0 and diff_str == 1) or (cnt_not_equil == 1 and diff_str == 0):
    print("True")
else:
    print("False")
