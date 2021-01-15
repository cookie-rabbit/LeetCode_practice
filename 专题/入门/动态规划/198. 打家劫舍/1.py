# https://leetcode-cn.com/problems/house-robber/
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
#
#  
#
# 示例 1：
#
# 输入：[1,2,3,1]
# 输出：4
# 解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
#      偷窃到的最高金额 = 1 + 3 = 4 。
# 示例 2：
#
# 输入：[2,7,9,3,1]
# 输出：12
# 解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
#      偷窃到的最高金额 = 2 + 9 + 1 = 12 。
from typing import List


class Solution:
    # 标准 dp 表解法
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = len(nums)
        dp = [0] * k
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2, k + 1):
            # 偷最后一间房 dp[i - 1],不偷最后一间而是偷前一间 dp[i - 2] + nums[i - 1](最后一次也就是 nums[k])
            dp[i] = max(dp[i - 1], nums[i - 1] + dp[i - 2])
        return dp[k]

    # 空间优化
    def rob2(self, nums: List[int]) -> int:
        prev = 0
        curr = 0

        # 每次循环，计算“偷到当前房子为止的最大金额”
        for i in nums:
            # 循环开始时，curr 表示 dp[k-1]，prev 表示 dp[k-2]
            # dp[k] = max{ dp[k-1], dp[k-2] + i }
            prev, curr = curr, max(curr, prev + i)
            # 循环结束时，curr 表示 dp[k]，prev 表示 dp[k-1]

        return curr
