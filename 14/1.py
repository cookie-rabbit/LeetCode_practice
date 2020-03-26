from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        bb = zip(*strs)
        print(bb)
        for i in zip(*strs):
            if len(set(i)) == 1:
                s += i[0]
            else:
                break
        return s


a = Solution().longestCommonPrefix(["flower", "flow", "flight"])
print(a)
