
class Solution:
    def plusOne(self, digits):
        s = int("".join(str(i) for i in digits))+1
        ss = [int(i) for i in list(str(s))]
        return ss


s = Solution().plusOne([0, 1, 4, 5, 0,4])
print(s)
