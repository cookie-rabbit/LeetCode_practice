# https://leetcode-cn.com/problems/valid-anagram/
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#
# 示例 1:
#
# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 示例 2:
#
# 输入: s = "rat", t = "car"
# 输出: false
# 说明:
# 你可以假设字符串只包含小写字母。
#
# 进阶:
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
import collections


class Solution:
    # 利用 ASCII 码进行判断
    # 不过文本太短，非常容易出现两个文本恰好加起来等于一个数字，所以可以设计一种函数，将字母对应的ASCII变换一下，
    # 可以使用**2（不过貌似被出题人写了对应的测试案例过不了），好的函数是可以使两对文本相加恰好相等的概率降至极低
    def isAnagram2(self, s: str, t: str) -> bool:
        return abs(sum([ord(x) ** 0.5 for x in s]) - sum([ord(y) ** 0.5 for y in t])) < 1e-5

    # 直接比较哈希表(利用函数效率更高)
    def isAnagram(self, s: str, t: str) -> bool:
        a = collections.Counter(s)
        b = collections.Counter(t)
        if a == b:
            return True
        else:
            return False
