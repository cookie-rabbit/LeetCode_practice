# 核心思路，当当前值加下一个值小于下一个值本身，即当前值为负时，本子数组结束，以下一个值作为开始。
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        return bin(a + b)[2:]


s = Solution().addBinary("1010", "1011")
print(s)
