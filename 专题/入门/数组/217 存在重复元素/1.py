# https://leetcode-cn.com/problems/contains-duplicate/solution/
# 给定一个整数数组，判断是否存在重复元素。
#
# 如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
#
#
# 示例 1:
#
# 输入: [1,2,3,1]
# 输出: true
# 示例 2:
#
# 输入: [1,2,3,4]
# 输出: false
# 示例 3:
#
# 输入: [1,1,1,3,3,4,3,2,4,2]
# 输出: true
from typing import List


class Solution:
    # 直接用 set 方法处理掉重复，然后对比元素个数
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        if len(nums) != len(set(nums)):
            return True
        else:
            return False

    # 遍历比较，效率不如1
    def containsDuplicate2(self, nums: List[int]) -> bool:
        if not nums:
            return False
        nums.sort()
        i = 1
        while i <= len(nums) - 1:
            if nums[i] - nums[i - 1] == 0:
                return True
            i += 1
        return False

    # 还可以用 in 去遍历，但是效率可能更低
