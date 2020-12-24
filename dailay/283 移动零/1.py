# https://leetcode-cn.com/problems/move-zeroes/
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 示例:
#
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 说明:
#
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。


from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        number = nums.count(0)
        for i in range(number):
            nums.remove(0)
            nums.append(0)


class Solution2:
    # 双指针法，left 指向整理好的数列末尾，right 指向还没整理的数列队首
    # 每次 right 指向一个非 0 整数，left 和 right 指针指向的数字互换，同时 left 向右移动一位
    # 这样当 right 走到队尾时，所有的非零数都被按顺序交换到了队首。
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1

        #   或者更简单的
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1


    # 比较第一个0的位置，当最后面n个数均为0时结束,效率不高
    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if 0 not in nums:
            return

        counts = nums.count(0)

        while len(set(nums[-counts:])) != 1 or list(set(nums[-counts:]))[0] != 0:
            index = nums.index(0)
            nums.pop(index)
            nums.append(0)
