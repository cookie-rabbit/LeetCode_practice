# https://leetcode-cn.com/problems/shuffle-an-array/
# 给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。
#
# 实现 Solution class:
#
# Solution(int[] nums) 使用整数数组 nums 初始化对象
# int[] reset() 重设数组到它的初始状态并返回
# int[] shuffle() 返回数组随机打乱后的结果
#  
#
# 示例：
#
# 输入
# ["Solution", "shuffle", "reset", "shuffle"]
# [[[1, 2, 3]], [], [], []]
# 输出
# [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]
#
# 解释
# Solution solution = new Solution([1, 2, 3]);
# solution.shuffle();    // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。例如，返回 [3, 1, 2]
# solution.reset();      // 重设数组到它的初始状态 [1, 2, 3] 。返回 [1, 2, 3]
# solution.shuffle();    // 随机返回数组 [1, 2, 3] 打乱后的结果。例如，返回 [1, 3, 2]
#  
#
# 提示：
#
# 1 <= nums.length <= 200
# -106 <= nums[i] <= 106
# nums 中的所有元素都是 唯一的
# 最多可以调用 5 * 104 次 reset 和 shuffle
import copy
import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        """copy 和 deepcopy"""
        # copy对于一个复杂对象的子对象并不会完全复制，什么是复杂对象的子对象呢？就比如序列里的嵌套序列，
        # 字典里的嵌套序列等都是复杂对象的子对象。对于子对象，python会把它当作一个公共镜像存储起来，
        # 所有对他的复制都被当成一个引用，所以说当其中一个引用将镜像改变了之后另一个引用使用镜像的时候镜像已经被改变了。

        # deepcopy的时候会将复杂对象的每一层复制一个单独的个体出来。

        # 注意这里要 copy 一下，否则后面的修改会影响到 self.origin,用 deepcopy 也行,不过这里结构简单就无所谓了
        self.origin = copy.copy(nums)
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.origin

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.nums) - 1, 0, -1):
            pivot = random.randint(0, i)  # 前闭后闭
            self.nums[i], self.nums[pivot] = self.nums[pivot], self.nums[i]
        return self.nums
