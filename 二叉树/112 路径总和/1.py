from copy import deepcopy

from 二叉树.tree_node import TreeNode


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # 处理空值，注意没有内容时的和不是0而是 False,而 False 不等于0，所以返回为 False
        if root is None:
            return False
        ans = self.append_tree(root, [], sum)
        if ans:
            return True
        return False

    def append_tree(self, root, a, sum):
        a.append(root.val)
        s = None
        c = None
        if root.left:
            s = self.append_tree(root.left, deepcopy(a), sum)
        if root.right:
            c = self.append_tree(root.right, deepcopy(a), sum)
        # 两边都没，说明是叶节点，此时进行该分支计算
        if root.left is None and root.right is None:
            # 变量叫sum，禁用了sum()
            total = 0
            for i in a:
                total += i
            if total == sum:
                return True
        if s or c:
            return True


# 精简版
class Solution2:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

