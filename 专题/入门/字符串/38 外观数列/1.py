# https://leetcode-cn.com/problems/count-and-say/
# 给定一个正整数 n ，输出外观数列的第 n 项。
#
# 「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。
#
# 你可以将其视作是由递归公式定义的数字字符串序列：
#
# countAndSay(1) = "1"
# countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。
# 前五项如下：
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 第一项是数字 1
# 描述前一项，这个数是 1 即 “ 一 个 1 ”，记作 "11"
# 描述前一项，这个数是 11 即 “ 二 个 1 ” ，记作 "21"
# 描述前一项，这个数是 21 即 “ 一 个 2 + 一 个 1 ” ，记作 "1211"
# 描述前一项，这个数是 1211 即 “ 一 个 1 + 一 个 2 + 二 个 1 ” ，记作 "111221"
# 要 描述 一个数字字符串，首先要将字符串分割为 最小 数量的组，每个组都由连续的最多 相同字符 组成。然后对于每个组，先描述字符的数量，然后描述字符，形成一个描述组。要将描述转换为数字字符串，先将每组中的字符数量用数字替换，再将所有描述组连接起来。
#
# 示例 1：
#
# 输入：n = 1
# 输出："1"
# 解释：这是一个基本样例。
#
# 示例 2：
#
# 输入：n = 4
# 输出："1211"
# 解释：
# countAndSay(1) = "1"
# countAndSay(2) = 读 "1" = 一 个 1 = "11"
# countAndSay(3) = 读 "11" = 二 个 1 = "21"
# countAndSay(4) = 读 "21" = 一 个 2 + 一 个 1 = "12" + "11" = "1211"
import re


class Solution:
    # 描述前一项
    def countAndSay(self, n: int) -> str:
        pre = ''
        cur = '1'

        # 从第 2 项开始
        for _ in range(1, n):
            # 这里注意要将 cur 赋值给 pre
            # 因为当前项，就是下一项的前一项。有点绕，尝试理解下
            pre = cur
            # 这里 cur 初始化为空，重新拼接
            cur = ''
            # 定义双指针 start，end
            start = 0
            end = 0
            # 开始遍历前一项，开始描述
            while end < len(pre):
                # 统计重复元素的次数，出现不同元素时，停止
                # 记录出现的次数，
                while end < len(pre) and pre[start] == pre[end]:
                    end += 1
                # 元素出现次数与元素进行拼接
                cur += str(end - start) + pre[start]
                # 这里更新 start，开始记录下一个元素
                start = end

        return cur

    # 递归
    def countAndSay2(self, n: int) -> str:
        if n == 1:
            return '1'
        s = self.countAndSay2(n - 1)

        i, res = 0, ''
        for j, c in enumerate(s):
            if c != s[i]:
                res += str(j - i) + s[i]
                i = j
        res += str(len(s) - i) + s[-1]  # 最后一个元素莫忘统计
        return res

    # 迭代
    def countAndSay3(self, n: int) -> str:
        res = '1'
        for _ in range(n - 1):  # 控制循环次数
            i, tmp = 0, ''
            for j, c in enumerate(res):
                if c != res[i]:
                    tmp += str(j - i) + res[i]
                    i = j
            res = tmp + str(len(res) - i) + res[-1]
        return res

    # 正则表达式
    def countAndSay4(self, n: int) -> str:
        if n == 1:
            return '1'
        s = self.countAndSay4(n - 1)

        p = r'(\d)\1*'
        pattern = re.compile(p)
        res = [_.group() for _ in pattern.finditer(s)]  # 提取结果
        return ''.join(str(len(c)) + c[0] for c in res)  # join 内部的 str(len(c)) + c[0] for c in res 是生成器类型

    # 元素替换
    def countAndSay5(self, n: int) -> str:
        res = '1'
        p = r'(\d)\1*'
        pattern = re.compile(p)
        for _ in range(n - 1):
            res = pattern.sub(lambda x: str(len(x.group())) + x.group(1), res)  # 替换
        return res
