class Solution:
    def plus_one(self, num, i):
        if i == 1:
            plus = 'I'
        elif i == 2:
            plus = 'X'
        elif i == 3:
            plus = 'C'
        elif i == 4:
            plus = 'M'
        res = ''
        while num != 0:
            res += plus
            num -= 1
        return res

    def intToRoman(self, num: int) -> str:
        result = ''
        i = 0
        while num > 0:
            i += 1
            new_num = num % 10
            if new_num == 4:
                if i == 1:
                    result = 'IV' + result
                if i == 2:
                    result = 'XL' + result
                if i == 3:
                    result = 'CD' + result
            elif new_num in [0, 1, 2, 3]:
                result = self.plus_one(new_num, i) + result
            elif new_num - 5 in [0, 1, 2, 3]:
                result = self.plus_one(new_num - 5, i) + result
                if i == 1:
                    result = 'V' + result
                if i == 2:
                    result = 'L' + result
                if i == 3:
                    result = 'D' + result
            elif new_num == 9:
                if i == 1:
                    result = 'IX' + result
                if i == 2:
                    result = 'XC' + result
                if i == 3:
                    result = 'CM' + result
            num //= 10
        return result

