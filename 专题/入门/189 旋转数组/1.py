# https://leetcode-cn.com/problems/rotate-array/solution/xuan-zhuan-shu-zu-by-leetcode/
# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
#
# 示例 1:
# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]

# 示例2:
# 输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释:
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]
# 说明:
#
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 要求使用空间复杂度为O(1) 的原地算法。
from typing import List


class Solution:
    # 方法1，截取，交换,效率好
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 注意 k 可能超过数组长度，要用取余的方法处理下
        k %= len(nums)
        # 因为 k 的长度问题，如果右侧结果直接用 k 可能长度不够放下所有值
        nums[:k], nums[k:] = nums[len(nums) - k:], nums[:len(nums) - k]

    # 方法2，强制交换，效率差
    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        for _ in range(k):
            nums[1:], nums[:1] = nums[:-1], nums[-1:]

    # 先添加后删除
    def rotate3(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        for _ in range(k):
            nums.insert(0, nums[-1])
            nums.pop(-1)

    # 还有一个环状替换法，但是需要额外变量，这里不符合题意


ss = [1, 2, 3, 4, 5, 6, 7]
Solution().rotate3(ss, 3)
print(ss)
