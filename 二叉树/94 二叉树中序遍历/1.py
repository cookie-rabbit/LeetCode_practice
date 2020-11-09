# 给你二叉树的根节点 root ，返回它节点值的 中序 遍历。
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
from typing import List
from 二叉树.tree_node import TreeNode

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ss = []
        def preorder(root: TreeNode):
            if not root:
                return root
            ss.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return ss
