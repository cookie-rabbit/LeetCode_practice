# https://leetcode-cn.com/problems/number-of-islands/solution/
# 给你一个由'1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
#
# 此外，你可以假设该网格的四条边均被水包围。
#
# 示例 1：
#
# 输入：grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# 输出：1
#
# 示例 2：
#
# 输入：grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# 输出：3
#
# 提示：
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] 的值为 '0' 或 '1'
from typing import List


class Solution:
    # 深度优先查法
    def dfs(self, grid, r, c):
        # 关键，将找到的点值改为 0，并搜索与其直接相连的点全部置为 0.
        grid[r][c] = 0
        # 输入矩形宽 nr，长 nc
        nr, nc = len(grid), len(grid[0])
        # 检查目标点周围是否还有值为1的点，有就继续找下去，同时将该点值改为0，这样保证外层主函数每次找到的 1 都必然属于一个新的岛屿
        for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                self.dfs(grid, x, y)

    def numIslands(self, grid: List[List[str]]) -> int:
        # grid 是一个有 nr 列，每列 nc 个元素的矩形
        # 即输入矩形宽 nr，长 nc
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        # 初始化岛屿数量
        num_islands = 0

        # 先循环列
        for r in range(nr):

            # 循环每列的每行
            for c in range(nc):
                # 如果该点的值为1，岛屿 +1
                if grid[r][c] == "1":
                    num_islands += 1
                    self.dfs(grid, r, c)

            return num_islands