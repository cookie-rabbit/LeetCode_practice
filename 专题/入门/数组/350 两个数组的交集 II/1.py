# https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/
# 给定两个数组，编写一个函数来计算它们的交集。
#
# 示例 1：
# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2,2]
#
# 示例 2:
# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[4,9]
#
#
# 说明：
# 输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
# 我们可以不考虑输出结果的顺序。
# 进阶：
#
# 如果给定的数组已经排好序呢？你将如何优化你的算法？
# 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
# 如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
import collections
from typing import List


class Solution:
    # 笨方法，拿出值一个个比较
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []

        nums = collections.deque(nums1)
        ss = []
        while nums:
            i = nums.popleft()
            if i in nums2:
                ss.append(i)
                nums2.remove(i)
        return ss

    # 切割法，每次切割掉被比较数组无关的部分，可以在大数据量时加快速度
    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []

        ss = []
        nums1.sort()
        nums2.sort()
        for i in nums1:
            if i in nums2:
                index = nums2.index(i)
                nums2 = nums2[index:]
                nums2.remove(i)
                ss.append(i)
        return ss

print(Solution().intersect([1, 2, 2, 1], [2, 2]))
