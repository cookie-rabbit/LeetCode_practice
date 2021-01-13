# https://leetcode-cn.com/problems/climbing-stairs/solution/70zhong-quan-chu-ji-python3hui-ji-liao-ti-jie-qu-w/
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
# 注意：给定 n 是一个正整数。
#
# 示例 1：
#
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
#
#
# 示例 2：
#
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶


# 直接递归解法，容易超时，python可以加个缓存装饰器，这样也算是将递归转换成迭代的形式了
# 除了这种方式，还有增加步长来递归，变相的减少了重复计算
# 还有一种方法，在递归的同时，用数组记忆之前得到的结果，也是减少重复计算
import functools


class Solution:
    @functools.lru_cache(100)  # 缓存装饰器
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# 直接DP，新建一个字典或者数组来存储以前的变量，空间复杂度O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


# 还是DP，只不过是只存储前两个元素，减少了空间，空间复杂度O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        a, b, temp = 1, 2, 0
        for i in range(3, n + 1):
            temp = a + b
            a = b
            b = temp
        return temp


# 直接斐波那契数列的计算公式喽
class Solution:
    def climbStairs(self, n: int) -> int:
        import math
        sqrt5 = 5 ** 0.5
        fibin = math.pow((1 + sqrt5) / 2, n + 1) - math.pow((1 - sqrt5) / 2, n + 1)
        return int(fibin / sqrt5)


# 面向测试用例编程
class Solution:
    def climbStairs(self, n: int) -> int:
        a = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657,
             46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465,
             14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170,
             1836311903]
        return a[n - 1]
