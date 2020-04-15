import time

# 默认的暴力解法，一个一个循环下去，但问题在于进行了大量的重复递归
def febo(n):
    if n == 1 or n == 2:
        return 1
    return febo(n - 1) + febo(n - 2)


start = time.time()
a = febo(35)
print(a)
end = time.time()
print(end - start)


# 带备忘录的递归法，当有备忘录时，所有已记录的递归树不需要重复递归
def febo2(n):
    if n < 1:
        return 0
    ss = [0 for i in range(n+1)]
    return helper(ss, n)


def helper(ss, n):
    if n == 1 or n == 2:
        return 1
    if ss[n] != 0:
        return ss[n]
    ss[n] = helper(ss, n - 1) + helper(ss, n - 2)
    return ss[n]


start = time.time()
b = febo2(35)
print(b)
end = time.time()
print(end - start)
