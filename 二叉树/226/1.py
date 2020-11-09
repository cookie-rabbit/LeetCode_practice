# 翻转一棵二叉树。
#
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

# 定义二叉树
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # ->常常出现在python函数定义的函数名后面，为函数添加元数据,描述函数的返回类型 对函数变量的描述和函数返回值的描述符号均只适用于Python3
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root
