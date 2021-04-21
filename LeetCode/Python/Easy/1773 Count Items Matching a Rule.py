from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        dct = {"type": 0,
               "color": 1,
               "name": 2}
        result = 0
        for i in items:
            if ruleValue == i[dct[ruleKey]]:
                result += 1
        return result
