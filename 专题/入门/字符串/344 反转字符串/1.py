# https://leetcode-cn.com/problems/reverse-string/
# 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
#
# 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
#
# 你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。
#
# 示例 1：
#
# 输入：["h","e","l","l","o"]
# 输出：["o","l","l","e","h"]
# 示例 2：
#
# 输入：["H","a","n","n","a","h"]
# 输出：["h","a","n","n","a","H"]
from typing import List


class Solution:
    # 直接交换，交换次数为数组长度除以2的整数商
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s:
            return

        times = len(s) // 2
        for i in range(times):
            s[i], s[-(i + 1)] = s[-(i + 1)], s[i]

    #  简化方案
    def reverseString2(self, s: List[str]) -> None:
        s[:] = s[::-1]

    # 双指针
    def reverseString3(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    # python 有个 reverse 函数，可以直接翻转列表
