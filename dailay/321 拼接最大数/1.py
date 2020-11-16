# https://leetcode-cn.com/problems/create-maximum-number/
# 给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。现在从这两个数组中选出 k (k <= m + n) 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。
#
# 求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。
#
# 说明: 请尽可能地优化你算法的时间和空间复杂度。
#
# 示例 1:
#
# 输入:
# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
# 输出:
# [9, 8, 6, 5, 3]
# 示例 2:
#
# 输入:
# nums1 = [6, 7]
# nums2 = [6, 0, 4]
# k = 5
# 输出:
# [6, 7, 6, 0, 4]
# 示例 3:
#
# 输入:
# nums1 = [3, 9]
# nums2 = [8, 9]
# k = 3
# 输出:
# [9, 8, 9]

from typing import List

nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5


# 标准答案
# def maxNumber(nums1: List[int], nums2: List[int], k: int) -> List[int]:
#     def merge_max(A: List[int], B: List[int]):
#         ans = []
#         while A or B:
#             bigger = A if A > B else B
#             ans.append(bigger[0])
#             bigger.pop(0)
#         return ans
#
#     def find_max(a: List[int], k: int) -> List[int]:
#         stack = []
#         l = len(a) - k
#         for i in a:
#             while stack and l > 0 and i > stack[-1]:
#                 stack.pop()
#                 l -= 1
#             stack.append(i)
#         return stack[:k]
#
#     return max(merge_max(find_max(nums1, i), find_max(nums2, k - i)) for i in range(k + 1) if
#                i <= len(nums1) and k - i <= len(nums2))

# 自己做的
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        # 对每个列表按不同的k的分配找出本列表最大值，再组装成最大的组合，最后把所有k分配不同情况下得出的组合做比较
        ss = []
        for i in range(k + 1):
            # 注意边界，要有等于号，否则当 k 刚好等于两个列表长度之和时判断条件会不成立，导致ss为空。
            # 但是不需要考虑两个数组为空的情况，因为 k <= m + n, 如果 m 和 n 任一空，则 k 不存在，本题会出现逻辑错误。
            if i <= len(nums1) and k - i <= len(nums2):
                s = []
                s1 = self.find_max(nums1, i)
                s2 = self.find_max(nums2, k - i)
                # 找出两个列表组合的最大值，其实和下面的移除函数从思路上是一样的
                # 比较两个列表当前位，选出最大值放入新列表，因为长度恰好为 k，所以应该循环到两个列表都为空
                while s1 or s2:
                    bigger = s1 if s1 > s2 else s2
                    s.append(bigger[0])
                    bigger.pop(0)
                ss.append(s)
        # 将得到的所有列表进行比较，选取最大的
        return max(ss)

    # 402 题反转，移除 k 位数字，找出最大值
    def find_max(self, a: List[int], k: int) -> List[int]:
        stack = []
        l = len(a) - k
        for i in a:
            while stack and l > 0 and i > stack[-1]:
                stack.pop()
                l -= 1
            stack.append(i)
        return stack[:k]
