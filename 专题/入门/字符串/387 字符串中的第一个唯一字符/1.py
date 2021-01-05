# https://leetcode-cn.com/problems/first-unique-character-in-a-string/
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
#
# 示例：
#
# s = "leetcode"
# 返回 0
#
# s = "loveleetcode"
# 返回 2
#  
#
# 提示：你可以假定该字符串只包含小写字母。
import collections


class Solution:
    # 暴力循环，效率低
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        for i_index, i in enumerate(s):
            for j_index, j in enumerate(s):
                if i == j and i_index != j_index:
                    break
            else:
                return i_index
        return -1

    # 哈希表
    def firstUniqChar2(self, s: str) -> int:
        if not s:
            return -1
        if len(s) == 1:
            return 0
        # 下面这段可以用 collections 的快速设置哈希表方法 ss = collections.Counter(s)，效率更高
        ss = {}
        for i in s:
            if i not in ss:
                ss.update({i: 1})
            else:
                ss[i] += 1

        ss = collections.Counter(s)

        for key, j in ss.items():
            if j == 1:
                return s.index(key)

        return -1


a = Solution().firstUniqChar2('loveleetcode')
print(a)
