# https://leetcode-cn.com/problems/longest-common-prefix/solution/
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 说明:
#
# 所有输入只包含小写字母 a-z 。

from typing import List


class Solution:
    # 解压缩，同时循环列表中的所有字符串，当各字符串在该位上的字母为同一个时，记录该字母，否则停止循环，返回结果
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        bb = zip(*strs)
        print(bb)
        for i in zip(*strs):
            if len(set(i)) == 1:
                s += i[0]
            else:
                break
        return s


a = Solution().longestCommonPrefix(["flower", "flow", "flight"])
print(a)
