class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        if strs == []:
            return result
        min = len(strs[0])
        word = strs[0]
        for i in range(len(strs)):
            if len(strs[i]) < min:
                min = len(strs[i])
                word = strs[i]
        for i in range(min):
            isEquil = True
            for item in strs:
                if word[i] != item[i]:
                    isEquil = False
                    break
            if isEquil:
                result += word[i]
            else:
                break
        return result
