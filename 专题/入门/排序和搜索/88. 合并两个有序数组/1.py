# https://leetcode-cn.com/problems/merge-sorted-array/
# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
#
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 有足够的空间（空间大小等于 m + n）来保存 nums2 中的元素。
#
#  
#
# 示例 1：
#
# 输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# 输出：[1,2,2,3,5,6]
# 示例 2：
#
# 输入：nums1 = [1], m = 1, nums2 = [], n = 0
# 输出：[1]
#  
#
# 提示：
#
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# nums1.length == m + n
# nums2.length == n
# -109 <= nums1[i], nums2[i] <= 109
import collections
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 这种方法实际中不会允许，要通过双指针来完成
        nums1[m:] = nums2
        nums1.sort()

        """
        https://leetcode-cn.com/problems/merge-sorted-array/solution/gelthin-gui-bing-pai-xu-by-gelthin/
        注意不能 nums1 = nums1 + nums2
        
        对于 python3 语言， 题目要求：Do not return anything, modify nums1 in-place instead.
        即，需要就地修改 nums1 对象，而不能新生成一个对象，并让 nums1 指向这一新对象。
        
        注意到 python3 语言, 对象是一个盒子，有具体的地址，而变量名相当于是 "标签"，可以贴在盒子上。
        
        我们需要辨析：nums1 = A 和 nums1[:] = A 的不同之处：
        
        nums1 = A # 更改 nums1 这一变量名所指向的对象。让 nums1 变量指向 A 所指向的对象
        nums1[:] = A # 对 nums1 指向的对象赋值。把 A 变量指向的对象的值逐个 copy 到 nums1 指向的对象中并覆盖 nums1 指向的对象的原来值。
        nums1[:] 等价于 nums1[0:len(nums1)] 相当于取 nums1 对应的对象的一个视图，通常用这个来改变原对象的某几位值。
        比如有时候，我们用 A[:2] = [0,1], 来改变 A 所指向的 list 对象的前两个值。
        而如果用 A = [0,1], 则是让 A 这一变量名指向新的 list 对象 [0,1]
        
        下面的代码则验证了上面的解释：
        # 对象在内存中的地址与id 一一对应，可以使用 id() 查看并判断是否是同一个对象
        
        nums1 = [1,2,4,0,0] 
        print(id(nums1)) # 140125129895880
        
        A = [1,2,3,4,5]
        print(id(A))     # 140125129856640
        
        nums1[:] = A
        print(id(nums1))) # 140125129895880,  仍是原 list 对象, 只不过这一 list 对象的值发生了改变
        
        # 若不执行 nums1[:] = A, 而执行
        nums1 = A
        print(id(nums1))  # 140125129856640, 不再是之前的那个 list 对象
        """

    # 比较法
    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        for j in nums2:
            for i in range(m):
                if j < nums1[i]:
                    nums1.insert(i, j)
                    nums1.pop()
                    m += 1
                    break
                if j >= nums1[m - 1]:
                    nums1.insert(m, j)
                    nums1.pop()
                    m += 1
                    break

    # 双指针，利用了 m 和 n 作为双指针，比较得到两个数组最大的元素，作为最大值放在最后
    def merge3(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m == 0:
            nums1[:] = nums2
        elif n == 0:
            pass
        else:
            while m != 0:
                # 从两个列表的末位数进行比较，因为 nums1 中必然有足够的位数，所以可以这么做
                if n > 0 and nums1[m - 1] < nums2[n - 1]:
                    nums1[m + n - 1] = nums2[n - 1]
                    n = n - 1
                else:
                    nums1[m + n - 1] = nums1[m - 1]
                    m = m - 1

            while n != 0:
                nums1[m + n - 1] = nums2[n - 1]
                n = n - 1
