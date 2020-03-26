from typing import List, Tuple


class Solution:
    def twoSum(self, nums: List[int], target: int) -> Tuple[int, int]:
        ss = []
        n = len(nums)
        for i in range(n):
            ss.append(i)
        d = dict(zip(nums, ss))
        for x in range(n):
            if target - nums[x] in nums:
                if d[target - nums[x]] == x:
                    pass
                else:
                    return x, d[target - nums[x]]
            else:
                d[nums[x]] = x


print(Solution().twoSum([3, 2, 4], 6))
