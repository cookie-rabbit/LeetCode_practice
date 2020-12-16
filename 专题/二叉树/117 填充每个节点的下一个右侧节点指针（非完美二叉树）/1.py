# https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/
# 给定一个二叉树
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
#
# 初始状态下，所有 next 指针都被设置为 NULL。
import collections

from 二叉树.tree_node import TreeNode


# 基本方法，一层层数过去，递归？（这个方法同样适用完美二叉树），117 题强化
class Solution:
    def connect(self, root: TreeNode) -> TreeNode:
        # 先处理异常
        if not root:
            return root

        # 初始化队列同时将第一层节点加入队列中，即根节点
        Q = collections.deque([root])

        # 外层的 while 循环迭代的是层数
        while Q:

            # 记录当前队列大小
            size = len(Q)

            # 遍历这一层的所有节点
            for i in range(size):

                # 从队首取出元素
                node = Q.popleft()

                # 连接，当 i 为最后一位数字的索引时，此时该数字已被取出并被前面的数字连接过了，Q 此时为空，不需要再连接了
                if i < size - 1:
                    node.next = Q[0]

                # 拓展下一层节点
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)

        # 返回根节点
        return root