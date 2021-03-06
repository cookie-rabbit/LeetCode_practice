# https://leetcode-cn.com/problems/count-complete-tree-nodes/
# 给出一个完全二叉树，求出该树的节点个数。
#
# 说明：
#
# 完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。
#
# 示例:
#
# 输入:
#     1
#    / \
#   2   3
#  / \  /
# 4  5 6
#
# 输出: 6
from 二叉树.tree_node import TreeNode

# 只问节点数，数出所有非叶节点的节点就可以了(但这种方法效率低)
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        return 1+self.countNodes(root.left)+self.countNodes(root.right)