# 翻转一棵二叉树。
# https://leetcode-cn.com/problems/invert-binary-tree/solution/226fan-zhuan-er-cha-shu-by-yi-wen-statistics/
# 示例：
#
# 输入：
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# 输出：
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1


from 二叉树.tree_node import TreeNode


class Solution:
    # ->常常出现在python函数定义的函数名后面，为函数添加元数据,描述函数的返回类型 对函数变量的描述和函数返回值的描述符号均只适用于Python3
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root
