# https://leetcode-cn.com/problems/validate-binary-search-tree/
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#
# 假设一个二叉搜索树具有如下特征：
#
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# 示例 1:
#
# 输入:
#     2
#    / \
#   1   3
# 输出: true
# 示例 2:
#
# 输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。
from tree_node import TreeNode


class Solution:
    # 迭代中序遍历，其实就是对一个父节点，他的左子节点必须小于他，右子节点必须大于他
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        p = root
        pre = None
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            # 注意 res 这里的转换，当 res 为非叶节点时，这里比较的是他的左侧必须小于他
            # 而当 res 为右侧子节点时，比较的是右侧子节点的值不能小于等于他的父节点
            res = stack.pop()
            if pre and res.val <= pre.val:
                return False
            pre = res
            p = res.right
        return True

    # 递归中序遍历
    def isValidBST2(self, root: TreeNode) -> bool:
        self.pre = None

        def isBST(root):
            if not root:
                return True
            # 传递 False 状态
            if not isBST(root.left):
                return False

            if self.pre and self.pre.val >= root.val:
                return False
            self.pre = root
            # print(root.val)
            return isBST(root.right)

        return isBST(root)
