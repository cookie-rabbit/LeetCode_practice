# 核心思路，当当前值加下一个值小于下一个值本身，即当前值为负时，本子数组结束，以下一个值作为开始。
class Solution:
    def maxSubArray(self, nums) -> int:
        a, b = nums[0], nums[0]
        for i in nums[1:]:
            a = a + i if a >= 0 else i
            b = b if b > a else a
        return b


s = Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(s)
