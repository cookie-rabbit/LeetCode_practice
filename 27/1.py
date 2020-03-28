from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i <= len(nums) - 1:
            if nums[i] == val:
                del nums[i]
            else:
                i += 1
        return len(nums)
