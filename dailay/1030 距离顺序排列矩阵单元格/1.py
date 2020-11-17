# https://leetcode-cn.com/problems/matrix-cells-in-distance-order/
# 给出 R 行 C 列的矩阵，其中的单元格的整数坐标为 (r, c)，满足 0 <= r < R 且 0 <= c < C。
#
# 另外，我们在该矩阵中给出了一个坐标为 (r0, c0) 的单元格。
#
# 返回矩阵中的所有单元格的坐标，并按到 (r0, c0) 的距离从最小到最大的顺序排，其中，
# 两单元格(r1, c1) 和 (r2, c2) 之间的距离是曼哈顿距离，|r1 - r2| + |c1 - c2|。
# （你可以按任何满足此条件的顺序返回答案。）
#
# 示例 1：
#
# 输入：R = 1, C = 2, r0 = 0, c0 = 0
# 输出：[[0,0],[0,1]]
# 解释：从 (r0, c0) 到其他单元格的距离为：[0,1]
# 示例 2：
#
# 输入：R = 2, C = 2, r0 = 0, c0 = 1
# 输出：[[0,1],[0,0],[1,1],[1,0]]
# 解释：从 (r0, c0) 到其他单元格的距离为：[0,1,1,2]
# [[0,1],[1,1],[0,0],[1,0]] 也会被视作正确答案。
# 示例 3：
#
# 输入：R = 2, C = 3, r0 = 1, c0 = 2
# 输出：[[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
# 解释：从 (r0, c0) 到其他单元格的距离为：[0,1,1,2,2,3]
# 其他满足题目要求的答案也会被视为正确，例如 [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]]。
import collections
from typing import List


class Solution:
    # 自己的做法:找出所有元素，比较距离后按距离从小到大排序。
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        # ss = [(i, j) for i in range(R) for j in range(C)] 这么写一行解决
        ss = []
        for i in range(R):
            for j in range(C):
                ss.append([i, j])
        # 用曼哈顿法排序
        ss.sort(key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))
        return ss


a = Solution().allCellsDistOrder(3, 4, 5, 6)
print(a)


class Solution2:
    # 桶排序，也叫箱排序。桶排序的要求是数据的长度必须完全一样。（没看懂）
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        maxDist = max(r0, R - 1 - r0) + max(c0, C - 1 - c0)
        bucket = collections.defaultdict(list)
        dist = lambda r1, c1, r2, c2: abs(r1 - r2) + abs(c1 - c2)

        for i in range(R):
            for j in range(C):
                bucket[dist(i, j, r0, c0)].append([i, j])

        ret = list()
        for i in range(maxDist + 1):
            ret.extend(bucket[i])

        return ret
