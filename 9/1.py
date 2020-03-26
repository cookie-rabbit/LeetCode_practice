class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        if x > 0:
            if x % 10 == 0:
                return False
            y, res = x, 0
            while y != 0:
                res = res * 10 + y % 10
                y //= 10
            if x == res:
                return True
            else:
                return False


a = Solution().isPalindrome(999)
print(a)
