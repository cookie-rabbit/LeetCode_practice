# 给定一个以字符串表示的非负整数  num，移除这个数中的 k 位数字，使得剩下的数字最小。
# https://leetcode-cn.com/problems/remove-k-digits/
# 注意:
# num 的长度小于 10002 且  ≥ k。
# num 不会包含任何前导零。
#
#
# 示例 1 :
# 输入: num = "1432219", k = 3
# 输出: "1219"
# 解释: 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219。
#
# 示例 2 :
# 输入: num = "10200", k = 1
# 输出: "200"
# 解释: 移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
#
# 示例 3 :
# 输入: num = "10", k = 2
# 输出: "0"
# 解释: 从原数字移除所有的数字，剩余为空就是 0。
# https://leetcode-cn.com/problems/remove-k-digits/

# 316，高级变体

class Solution(object):
    # 整体思路是，拿数字的每一位和左边的前一位作比较，如果该位更小，则整体数字更小，同时弹出前一位
    def removeKdigits(self, num, k):
        # 建一个列表用来装要留下的数字
        stack = []
        remain = len(num) - k
        for i in num:
            # 如果还要删数字，同时该位比左边前一位数字更小则弹出前一位数字，同时删数字要求减1
            while k and stack and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)
        #     注意，当 num 是一个类似 12345678 这样的每位递增数字时，上面的过滤条件无效，
        #     此时直接过滤掉最后几位就好（因为递增所以后几位一定是最大的）
        return "".join(stack[:remain]).lstrip('0') or '0'
