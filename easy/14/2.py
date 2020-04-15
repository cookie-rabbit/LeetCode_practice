from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            a = ""
            return a
        a = strs[0]
        for i in strs[1:]:
            while i.find(a) != 0:
                a = a[:-1]
        return a


a = Solution().longestCommonPrefix(["c", "acc", "ccc"])
print(a)
