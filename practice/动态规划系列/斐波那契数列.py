import time

# 方法一，默认的暴力解法，一个一个循环下去，但问题在于进行了大量的重复递归
"""暴力递归法，每个问题解决时间为O(1)，总计有2^n个问题，所以时间复杂度为O(2^n)，指数级别"""


def febo(n):
    if n == 1 or n == 2:
        return 1
    return febo(n - 1) + febo(n - 2)


# start = time.time()
# a = febo(1)
# print(a)
# end = time.time()
# print(end - start)


# 方法二，带备忘录的递归法，当有备忘录时，所有已记录的递归树不需要重复递归
# 递归法是从上向下进行计算的
"""备忘录递归法，每个问题解决时间为O(1)，总计有n个问题，所以时间复杂度为O(n)"""


# 这里用了循环创建ss列表，所以复杂度应为O(2n)?

def febo2(n):
    if n < 1:
        return 0
    ss = [0 for i in range(n + 1)]
    return helper(ss, n)


def helper(ss, n):
    if n == 1 or n == 2:
        return 1
    if ss[n] != 0:
        return ss[n]
    ss[n] = helper(ss, n - 1) + helper(ss, n - 2)
    return ss[n]


start = time.time()
b = febo2(50)
print(b)
end = time.time()
print(end - start)

# 方法三，使用dp表从底向上推算
# 动态规划是自底向上的
"""动态规划，每个问题解决时间为O(1)，总计有n个问题，所以时间复杂度为O(n)"""


def febo3(n):
    if n < 1:
        return 0
    ss = [0 for j in range(n + 1)]
    ss[1], ss[2] = 1, 1
    i = 3
    if n == 1 or n == 2:
        return ss[n]
    if n >= 3:
        for i in range(3, n + 1):
            ss[i] = ss[i - 1] + ss[i - 2]
        return ss[i]


start = time.time()
b = febo3(50)
print(b)
end = time.time()
print(end - start)

"""
得出状态转移方程
f(n)=1 if n=1,2
f(n)=f(n-2)+f(n-1) if n > 2
"""

"""进一步优化，状态转移其实只需要所求目标前两个值，所以可以优化空间复杂度到O(1)"""


def febo4(n):
    if n < 1:
        return 0
    pre, nex = 1, 1
    i = 3
    if n == 1 or n == 2:
        return 1
    if n >= 3:
        for i in range(3, n + 1):
            summ = pre + nex
            pre, nex = nex, summ
        return summ


start = time.time()
b = febo4(50)
print(b)
end = time.time()
print(end - start)
