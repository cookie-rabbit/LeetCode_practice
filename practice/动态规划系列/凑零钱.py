"""凑零钱问题，给定不限数量的指定面额的零钱（列表），和一个目标数（正整数），问凑到目标数值最少的零钱树木，如果无法完成，返回-1"""
import json
import time


def solution(ss, n):
    def dp(n):
        if n < 0:
            return -1
        if n == 0:
            return 0
        res = float("inf")
        for coin in ss:
            subpro = dp(n - coin)
            if subpro < 0:
                continue
            res = min(res, 1 + subpro)
        return res

    return dp(n)


"""
先列出动态转移方程
f(lists, n) = -1 if n<0
f(lists, n) = 0 if n=0
# 下面这句的意思是在f(n-list)+1中最小的，而list属于lists 
f(lists, n) = min{f(n-list)+1|list∈lists} if n>0    
"""


def solution2(ss, n):
    ssc = {1: 1, 2: 1}

    def dp(n):

        if n < 0:
            return -1
        if n == 0:
            return 0

        if n in ssc.keys():
            return ssc[n]

        res = float("inf")
        """
        # 自顶向下的计算方法，比较当前方法和再多用任意一个硬币时的方法的所需硬币和
        # 这一段代码其实是把所有可能性列出来，并进行比较
        举例：当n=12，list=[1,2,5]：
        可能性为：
            当coin为1，循环为：
            1+dp(11)
            此时相当于求dp(11)的值,一直递归下去后，可以得到：
            末尾节点一定是由dp(5),dp(2),dp(1)组成,其中dp(5),dp(2)，都可以拆到dp(1)组成
            因此，这段代码的本质：
            对给定金额用所有硬币组合进行尝试，对于可以拆分成更小组合的，不断拆下去，并比较拆分次数
            每拆分一次次数+1，最终，将所有组合比较得到拆分最少次数，也就是所需最少硬币的个数
            设立ssc表的目的，即在于对于一部分已经计算过的不再需要再次计算，可以直接查到，这样不会有冗余
            那么，一个问题的最多次计算即n次，处理一个子问题的时间为O(k)，k为与硬币种类数有关的常数，所以时间复杂度为O(n)
        """
        for coin in ss:
            subpro = dp(n - coin)
            if subpro < 0:
                continue
            res = min(res, 1 + subpro)
            """
            上面这句代码可以有更易读的写法
            get = 1 + subpro
            if get < res:
                res = get
            get储存最后一次计算的结果，res储存目前次数最少的结果
            subpro一直递归下去，最终得到dp(0)
            dp(7)=1+dp(6)
            dp(6)=1+dp(5)
            dp(5)=1+dp(0)
            dp(7)=1+1+1+0  这其实是面额1+1+5的解法，当然还有其他可能
            """
            ssc.update({n: res})
        return res

    return dp(n)


# start = time.time()
# a = solution([1, 2, 5], 35)
# print(a)
# end = time.time()
# print(end - start)
#
start = time.time()
b = solution2([1, 2, 5], 25)
print(b)
end = time.time()
print(end - start)


def solution3(ss, n):
    ssc = [n + 1 for i in range(n + 1)]

    if n < 0:
        return -1
    if n == 0:
        return 0
    ssc[0] = 0
    """
    由底向上指的是，先列出一个列表，然后从最底部ssc[0]开始计算，因为最底的值是知道的，所以不断向上推，直到达到目的
    即算出ssc[n]以前的每一个值，ssc[n-1],ssc[n-2]等，从而将它们加起来得到所需最小值
    对于每一个值，通过在各种额度组合中进行计算，得出组合的最小值，然后再用于上一轮的计算，从而始终保证得到最小的值
    """
    for j in range(0, len(ssc)):
        """
        对于下面一段代码，目的是找出一个数额在各种币值组合可能中所需数量最少的那一个
        对range范围内中的每一个值从小到大算上去，因为前一个的最小值已经得到，所以避免了无谓的计算，达到最优
        此处注意，因为ssc设定为一个n+1长度的数列，所以ssc[n]和ssc[j]其实是相等的
        """
        for coin in ss:
            if j - coin < 0:
                continue
            ssc[j] = min(ssc[j], 1 + ssc[j - coin])
    # 因为ssc设定为一个n+1长度的数列，所以ssc[n]和ssc[j]其实是相等的
    # 因此也可以写成ssc[j],但是当然，j不是本函数内的全局变量，因此pycharm会提示要求设置global j
    return ssc[n]


start = time.time()
b = solution3([1, 2, 5], 5)
print(b)
end = time.time()
print(end - start)
