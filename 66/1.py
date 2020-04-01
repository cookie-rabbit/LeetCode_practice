# 核心思路，当当前值加下一个值小于下一个值本身，即当前值为负时，本子数组结束，以下一个值作为开始。
class Solution:
    def plusOne(self, digits):
        s = int("".join(str(i) for i in digits))+1
        ss = [int(i) for i in list(str(s))]
        return ss


s = Solution().plusOne([0, 1, 4, 5, 0,4])
print(s)
