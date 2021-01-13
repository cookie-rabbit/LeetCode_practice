# https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/
# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
#
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
#
# 示例:
#
# 给定有序数组: [-10,-3,0,5,9],
#
# 一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5
from typing import List

from tree_node import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def make_tree(start_index, end_index):  # 只和长度有关
            # 首先判定我们的区间是否合理，即left_index要<=right_index
            # 当相等时，只有root会产生，不会产生左右小树
            if start_index > end_index:
                return None

            # 我这里变量名都写得比较长，目的是方便理解
            mid_index = (start_index + end_index) // 2
            this_tree_root = TreeNode(nums[mid_index])  # 做一个小树的root

            this_tree_root.left = make_tree(start_index, mid_index - 1)
            this_tree_root.right = make_tree(mid_index + 1, end_index)

            return this_tree_root  # 做好的小树

        return make_tree(0, len(nums) - 1)
        # 可以看到整个题解只和index有关，和数组里的具体数字无关，
        # 因为题目给出的“有序数列”帮助我们满足了“二叉搜索树”的条件。