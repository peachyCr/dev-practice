from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_hight = 0
        hight = 0
        for point in gain:
            hight += point
            if hight > max_hight:
                max_hight = hight
        return max_hight
