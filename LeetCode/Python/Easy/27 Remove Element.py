class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        end = len(nums)
        count = 0
        i = 0
        while i < end:
            if nums[i] == val:
                count += 1
                for j in range(i, end - 1):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                end -= 1
                i -= 1
            i += 1

        del nums[end:]
