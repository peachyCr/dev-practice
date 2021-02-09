class Solution:
    def isValid(self, s: str) -> bool:
        i = 0
        while i < len(s):
            seachingFor = ''
            if s[i] == ')':
                seachingFor = '('
            elif s[i] == '}':
                seachingFor = '{'
            elif s[i] == ']':
                seachingFor = '['
            if seachingFor:
                j = i - 1
                if i + 1 != len(s):
                    s = s[:i] + s[i+1:]
                else:
                    s = s[:i]
                i -= 1
                if  j < 0 or s[j] != seachingFor:
                    return False
                else:
                    s = s[:j] + s[j+1:]
                    i -= 1
                if i < 0:
                    i = -1
            i += 1
        if len(s) == 0:
            return True
        else:
            return False
