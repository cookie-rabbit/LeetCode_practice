# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
# 示例：
# 二叉树：[3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层次遍历结果：
#
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
import collections
from typing import List
from 二叉树.tree_node import TreeNode


# BFS 方案
class Solution_BFS(object):
    # 始终记住传入的是树，树有 val，left，right，三个属性，不要当做列表。
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 新建队列，并将整个二叉树放进去
        queue = collections.deque()
        # 注意这里是 append 方法，即将整个 root 作为一个对象放进去
        queue.append(root)
        res = []
        while queue:
            # 因为 root 是一个整体，所以第一轮循环时这里的 size 长度为 1.
            # 而之后为该层级子分支的数量。
            size = len(queue)
            level = []
            for _ in range(size):
                # 弹出树的一个分支（第一次时为初始树本身），并将 root 的 val 存入，同时添加它的两个子树添加到 queue 中。
                # 但注意，虽然弹出的是一整个树，但树的 val 是固定的一个值，即当前最上方的根节点，而不是列表。
                cur = queue.popleft()
                # 如果弹不出东西了就说明队列已经空了，跳出循环，此时 while 也不再满足条件，结束循环并返回
                if not cur:
                    continue
                level.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            if level:
                res.append(level)
        return res


# DFS 方案
class Solution_DFS(object):
    # 始终记住传入的是树，树有 val，left，right，三个属性，不要当做列表。
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.level(root, 0, res)
        return res

    def level(self, root, level, res):
        if not root:
            return root
        if len(res) == level:
            res.append([])
        res[level].append(root.val)
        if root.left:
            self.level(root.left, level + 1, res)
        if root.right:
            self.level(root.right, level + 1, res)
