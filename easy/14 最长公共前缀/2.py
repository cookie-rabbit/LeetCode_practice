from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            a = ""
            return a
        a = strs[0]
        for i in strs[1:]:
            """
            Python find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，
            则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。
            """
            # 这里固定找该字符串是否是从第一位开始的，如果不是就削除一位，直到找到或全部削除
            while i.find(a) != 0:
                a = a[:-1]
        return a


a = Solution().longestCommonPrefix(["c", "acc", "ccc"])
print(a)
