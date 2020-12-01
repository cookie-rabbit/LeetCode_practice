# https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/
# 给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
#
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


# 基本方法，一层层数过去，递归？（这个方法同样适用非完美二叉树）
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


# 迭代？总之就是先处理本层，处理完后将指针挪动一位以继续
class Solution2:
    def connect(self, root: TreeNode) -> TreeNode:

        # 空内容处理
        if not root:
            return root

        # 从根节点开始
        leftmost = root

        # 当该二叉树左边有值时（因为是完美二叉树，每个父节点一定有两个子节点）
        while leftmost.left:

            # 遍历这一层节点组织成的链表，为下一层的节点更新 next 指针
            head = leftmost
            # 当 head 不存在，则说明本层已经被遍历完了
            while head:

                # head.left 的链表下一位即是该叶节点相同父节点右边的子节点， head.right
                head.left.next = head.right

                # 如果本层还有其他元素，则本元素的右侧叶节点在链表的下一位即是本层下一个元素的左叶节点
                if head.next:
                    head.right.next = head.next.left

                # 指针向后移动，遍历本层所有节点
                head = head.next

            # 去下一层的最左的节点
            leftmost = leftmost.left

        return root
