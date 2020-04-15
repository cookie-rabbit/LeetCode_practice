from typing import List, Tuple


class Solution:
    def twoSum(self, nums: List[int], target: int) -> Tuple[int, int]:
        d = {}
        n = len(nums)
        for x in range(n):
            if target - nums[x] in d:
                return d[target - nums[x]], x
            else:
                d[nums[x]] = x


print(Solution().twoSum([2, 7, 11, 15], 9))
