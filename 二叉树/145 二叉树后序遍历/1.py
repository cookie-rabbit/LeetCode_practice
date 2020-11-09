# 给你二叉树的根节点 root ，返回它节点值的 后序 遍历。
# https://leetcode-cn.com/problems/binary-tree-postorder-traversal/solution/
from typing import List
from 二叉树.tree_node import TreeNode


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ss = []

        def postorder(root: TreeNode):
            if not root:
                return root
            postorder(root.left)
            postorder(root.right)
            ss.append(root.val)
        postorder(root)
        return ss
