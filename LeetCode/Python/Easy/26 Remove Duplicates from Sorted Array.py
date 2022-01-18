class Solution:
    def mv(self, j, nums, sli):
        while j < sli - 1:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            j += 1

    def removeDuplicates(self, nums: List[int]) -> int:
        sli = len(nums)
        i = 0
        while i >= 0 and i < sli:
            isEq = False
            fav = nums[i]
            j = i + 1
            while j < sli and nums[j] == fav:
                self.mv(j, nums, sli)
                sli -= 1
                isEq = True
            if isEq == True:
                i -= 1
            i += 1
        del nums[sli:]
        return sli
