# 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
# https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
from typing import List
from 二叉树.tree_node import TreeNode

class Solution:
    def midorderTraversal(self, root: TreeNode) -> List[int]:
        ss = []
        def midorder(root: TreeNode):
            if not root:
                return root
            midorder(root.left)
            ss.append(root.val)
            midorder(root.right)

        midorder(root)
        return ss
