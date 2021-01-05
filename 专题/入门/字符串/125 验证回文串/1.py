# https://leetcode-cn.com/problems/valid-palindrome/
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。
#
# 示例 1:
#
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 示例 2:
#
# 输入: "race a car"
# 输出: false
# “回文串”是一个正读和反读都一样的字符串，比如“level”或者“noon”等等就是回文串。


class Solution:
    #  暴力处理，效率极低
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        s = list(filter(str.isalnum, s))
        s = list(i.lower() for i in s)
        print(s)
        sss = list(reversed(s))
        return s == sss

    # 双指针，注意还是要处理掉非字母和数字，以及将大写字母转小写，效率高
    def isPalindrome2(self, s: str) -> bool:
        if not s:
            return True
        s = list(filter(str.isalnum, s))
        head = 0
        tail = len(s) - 1
        while head <= tail:
            if s[head].lower() != s[tail].lower():
                return False
            head += 1
            tail -= 1
        return True
