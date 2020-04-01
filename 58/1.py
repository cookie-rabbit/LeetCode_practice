class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split(" ")
        if a == "" or not a:
            return 0
        c = ""
        for i in a:
            if len(i) == 0:
                pass
            else:
                c = i
        l = len(c)

        return l


s = Solution().lengthOfLastWord(" a   b  ")
print(s)
