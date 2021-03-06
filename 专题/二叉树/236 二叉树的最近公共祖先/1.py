# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
#
# 例如，给定如下二叉树: root =[3,5,1,6,2,0,8,null,null,7,4]
#
# 示例 1:
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
#
# 示例2:
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出: 5
# 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
from 二叉树.tree_node import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 先排除异常情况
        if not root or root == p or root == q:
            return root

        # 对左右节点分别进行递归
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 如果左右节点都找不到符合要求的，返回空
        if not left and not right:
            return None  # 1.
        # 如果左边没找到，则一定在右边（注意这里的判断条件是递进的）
        if not left:
            return right  # 3.
        # 同上，右边没找到，则一定在左边
        if not right:
            return left  # 4.

        # 两边都找到，说明两边各有一个目标节点，则根节点符合目标。
        return root  # 2. if left and right:
