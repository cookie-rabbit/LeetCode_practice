# 给定一个二叉树，检查它是否是镜像对称的。
# https://leetcode-cn.com/problems/symmetric-tree/
import collections
from typing import List
from 二叉树.tree_node import TreeNode


# 递归法
class Solution:
    def is_symmetric(self, root: TreeNode) -> bool:
        # 当树为空时，返回 True
        if not root:
            return True
        return self.is_symmetric_leaf(root.left, root.right)

    def is_symmetric_leaf(self, left: TreeNode, right: TreeNode):
        # 当树的左右节点均为空时返回 True
        if left is None and right is None:
            return True
        # 当树的左右节点只有一个存在时返回 False，注意全为空的情况上面已经判断过了，因此此时如果 if 成立则有且必定只有一个为空
        if left is None or right is None:
            return False
        # 如果树的两个子节点不相等，则一定不对称，返回 False
        if left.val != right.val:
            return False
        else:
            # 否则分别对比两个节点的对称子树，只有当两个子树均对称时整个树才是对称的
            return self.is_symmetric_leaf(left.left, right.right) and self.is_symmetric_leaf(left.right, right.left)


# 迭代法
class Solution2:
    @staticmethod
    def is_symmetric(root: TreeNode) -> bool:
        # 当树为空时，返回 True
        if not root:
            return True
        # 引入一个队列，这是把递归程序改写成迭代程序的常用方法。
        queue = collections.deque()
        # 把第一对子节点当做元祖放入队列中
        queue.append((root.left, root.right))
        # 要将 queue 全部进行检查，所有的位置对称节点都相等才算对称
        while queue:
            # 注意用两个变量解压弹出的元祖
            left, right = queue.popleft()
            # 要将 queue 全部执行完才算结束，这点和递归不同，因为递归时如果两个子节点都为空则不会再有其他节点，
            # 而在迭代中，两个对称子节点都不存在并不说明其他节点一定不存在
            if left is None and right is None:
                continue
            # 当树的左右节点只有一个存在时返回 False，注意全为空的情况上面已经判断过了，因此此时如果 if 成立则有且必定只有一个为空
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            # 将对称节点放入，继续检查对称性
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))

        return True

# 递归，每层条件逐层检查，即前序遍历
# 迭代，与递归类似，只是多了一个列表用来装要检查的条件
