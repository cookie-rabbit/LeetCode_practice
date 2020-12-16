# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# 根据一棵树的前序遍历与中序遍历构造二叉树。
#
# 注意:
# 你可以假设树中没有重复的元素。
#
# 例如，给出
#
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
# 返回如下的二叉树：
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
import collections
from typing import List

from 二叉树.tree_node import TreeNode

# 和 106 题一样的解法，唯一不同点是这里把前序遍历变成了栈，然后从左边弹出
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None

            val = preorder.popleft()
            root = TreeNode(val)
            index = idx_map[val]
            # 注意传入的边界，不是 0 和 len(inorder) - 1 了
            root.left = helper(left, index - 1)
            root.right = helper(index + 1, right)

            return root

        preorder = collections.deque(preorder)
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)
