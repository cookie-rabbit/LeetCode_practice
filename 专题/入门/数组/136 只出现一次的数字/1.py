# https://leetcode-cn.com/problems/single-number/
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#
# 说明：
#
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
#
# 示例 1:
# 输入: [2,2,1]
# 输出: 1

# 示例 2:
# 输入: [4,1,2,1,2]
# 输出: 4
#
from typing import List


class Solution:
    # 笨方法，用了额外的变量
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        while nums:
            a = nums.pop(0)
            if a in nums:
                nums.pop(0)
            else:
                return a

    def singleNumber2(self, nums):
        if len(nums) == 1:  # 如果数组长度为1，则直接返回即可
            return nums[0]
        nums.sort()  # 对数组进行排序，使其相同元素靠在一起
        for i in range(1, len(nums), 2):  # 循环数组，验证前后是否相同，由于原始出现两次，因此可跳跃判断
            if nums[i - 1] != nums[i]:
                return nums[i - 1]
            if (i + 2) == len(nums):  # 判断单一元素在排序后数组的最后面
                return nums[-1]

    # 对每个元素删除两次，如果第二次报错说明该元素只出现了一次
    def singleNumber3(self, nums):
        while True:
            d = nums[0]
            nums.remove(d)
            try:
                nums.remove(d)
            except:
                return d
