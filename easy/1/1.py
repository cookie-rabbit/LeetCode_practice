import collections
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


    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <= 1:
            return None

        lists = collections.deque(nums)
        index_1 = 0
        while lists:

            head = lists.popleft()
            for i in lists:
                if head + i == target:
                    return [index_1, lists.index(i) + index_1 + 1]
            index_1 += 1
        return None


print(Solution().twoSum([3, 2, 4], 6))
