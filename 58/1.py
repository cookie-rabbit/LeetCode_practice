class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split(" ")
        if a == "" or not a:
            return 0
        c = ""
        for i in a:
            if not len(i) == 0:
                c = i
        l = len(c)

        return l


s = Solution().lengthOfLastWord(" a   b ")
print(s)
