# https://leetcode-cn.com/problems/gas-station/
# 在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
#
# 你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。
#
# 如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。
#
# 说明: 
#
# 如果题目有解，该答案即为唯一答案。
# 输入数组均为非空数组，且长度相同。
# 输入数组中的元素均为非负数。
# 示例 1:
#
# 输入:
# gas  = [1,2,3,4,5]
# cost = [3,4,5,1,2]
#
# 输出: 3
#
# 解释:
# 从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
# 开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
# 开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
# 开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
# 开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
# 开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
# 因此，3 可为起始索引。
# 示例 2:
#
# 输入:
# gas  = [2,3,4]
# cost = [3,4,3]
#
# 输出: -1
#
# 解释:
# 你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
# 我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
# 开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
# 开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
# 你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
# 因此，无论怎样，你都不可能绕环路行驶一周。

from typing import List

gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

# 笨方法，把跑道展开成一条线，能跑到最后的就是符合条件的
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            n = 0
            new_gas = gas[i:] + gas[:i]
            new_cost = cost[i:] + cost[:i]
            for j in range(len(gas)):
                n = n + new_gas[j] - new_cost[j]
                if n < 0:
                    break
            else:
                return i
        return -1

# 先排除油根本不够开的情况后，其他情况一定有解：
# 假设从头开始开一遍，累计下来耗油最多的点的后面那个点开始出发，一定就是跑完以后剩下油最多的。
# 即找出累计加油和累计油耗的差距最大的点，此时累计相对油耗最大，从这个点后面的那个点出发油一定够（已经排除了不够开的情况）。
class Solution2:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        left = [gas[i] - cost[i] for i in range(len(gas))]
        minValue = 999
        minIndex = 0

        sumValue = 0
        for j, l in enumerate(left):
            sumValue += l
            if sumValue < minValue:
                minValue = sumValue
                minIndex = j

        if sumValue < 0:
            return -1
        else:
            return (minIndex + 1) % len(gas)
