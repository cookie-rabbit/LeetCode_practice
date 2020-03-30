class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a = len(needle)
        b = len(haystack)
        for i in range(b - a + 1):
            s = haystack[i:i+a]
            if haystack[i:i+a+1] == needle:
                return i
        return -1


a = Solution().strStr("abcdeff", "ff")
print(a)
