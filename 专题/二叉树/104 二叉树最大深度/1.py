# 给定一个二叉树，找出其最大深度。
#
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#
# 说明: 叶子节点是指没有子节点的节点。
# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/

from 二叉树.tree_node import TreeNode


# 自顶向下解决方案，即前序遍历
class SolutionPreorder:
    answer = 0

    def maxDepth(self, root: TreeNode) -> int:
        def deep(root: TreeNode, depth: int):
            if not root:
                return root
            # 前序遍历的特征，当遇到叶子节点时立即更新数据，比较当前深度和记录最大深度的大小并选最大值记入最大深度
            if not (root.left or root.right):
                self.answer = max(self.answer, depth)
            deep(root.left, depth + 1)
            deep(root.right, depth + 1)

        deep(root, 1)
        return self.answer


# 自底向上解决方案，即后序遍历
class SolutionBackorder:
    # 注意，自底向上时不需要提前定义一个 answer，因为没有 a = a + b 这样的结构，当然也可以写,但属于浪费内存
    """
    answer = 0
    def maxDepth(self, root: TreeNode) -> int:
        def deep(root: TreeNode):
            if not root:
                return 0
            deep_left = deep(root.left)
            deep_right = deep(root.right)
            self.answer = max(deep_left,deep_right) + 1
            return self.answer
        deep(root)
        return self.answer
    """

    def maxDepth(self, root: TreeNode) -> int:
        def deep(root: TreeNode):
            # 注意这里不返回原内容即空，而是0，因为是自底向上计算的，不存在子节点则子节点的深度即为0而不是空
            if not root:
                return 0
            deep_left = deep(root.left)
            deep_right = deep(root.right)
            return max(deep_left, deep_right) + 1

        return deep(root)
