# https://leetcode-cn.com/problems/maximum-subarray/
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 进阶:
#
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

# 核心思路，当当前值加下一个值小于下一个值本身，即当前值为负时，本子数组结束，因为此时再加下去还不如下一个值本身的值大
# ，以下一个值作为新子数组的开始，将整个数组按照这个方法整理为数个子数组。
# 而一个子数组的每一步相加后都应该与当前的最大和比较一次，以记录和最大的情况。
from typing import List


class Solution:
    def maxSubArray(self, nums) -> int:
        # b 不能为 0 因为 nums 可能全都小于0
        a, b = nums[0], nums[0]
        for i in nums[1:]:
            a = a + i if a >= 0 else i
            b = b if b > a else a
        return b

    def maxSubArray2(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i - 1] + nums[i], nums[i])
        return max(nums)


s = Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(s)
