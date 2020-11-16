# 给你一个仅包含小写字母的字符串，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证返回结果的字典序最小
# （要求不能打乱其他字符的相对位置）。
# https://leetcode-cn.com/problems/remove-duplicate-letters/
# 示例 1:
#
# 输入: "bcabc"
# 输出: "abc"
# 示例 2:
#
# 输入: "cbacdcbc"
# 输出: "acdb"

# 加强版的 402 题
import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        # 用这个方法快速创建一个统计各元素出现次数的字典
        remain_counter = collections.Counter(s)

        for i in s:
            # 如果本字母没在 stack 中出现过则参与判断
            if i not in stack:
                # 如果当前字母比前一个字母小，弹出前一个字母，但是如果该字母只出现了一次，则不能弹出
                while stack and i < stack[-1] and remain_counter[stack[-1]] > 0:
                    stack.pop()
                # 添加本字母
                stack.append(i)
            remain_counter[i] -= 1
        return "".join(stack)


print(Solution().removeDuplicateLetters("leetcode"))
