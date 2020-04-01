
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        return bin(a + b)[2:]


s = Solution().addBinary("1010", "1011")
print(s)
