# https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/
# 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
#
# 请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
#
# 示例:
#
# 你可以将以下二叉树：
#
#     1
#    / \
#   2   3
#      / \
#     4   5
#
# 序列化为 "[1,2,3,null,null,4,5]"
# 提示:这与 LeetCode 目前使用的方式一致，详情请参阅LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。
#
# 说明:不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。
import collections

from tree_node import TreeNode


class Codec:

    # 序列化二叉树
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "[]"
        res = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            # 把节点自身放入，并将子节点放入队列末尾
            if node:
                queue.append(node.left)
                queue.append(node.right)
                res.append(node.val)
            else:
                # 否则放入一个空
                res.append(None)
        # 清理末尾的 None
        while res[-1] is None:
            res.pop()
        return str(res)

    # 反序列化
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # 异常处理
        if data == '[]':
            return None

        # li 是列表 data 从第二位开始到倒数第二位结束的截取片段，这是为了去掉字符串两边的 '[', ']'
        li = data[1:-1].split(',')
        queue = collections.deque()
        # 列表第一个节点即为根节点
        root = TreeNode(int(li[0]))
        queue.append(root)
        counter = 0
        # 从根节点的下一位开始截取
        for v in li[1:]:
            # 状态记录器（像寄存器），异或用来记录当前状态
            if counter == 0:
                parent = queue.popleft()
            if v.strip() != 'None':
                cur = TreeNode(int(v))
                queue.append(cur)
                if counter == 0:
                    parent.left = cur
                else:
                    parent.right = cur
            # 当 counter 为0，异或得出结果为1，否则为0
            # 这样用来判断是要放到左节点还是右节点
            counter ^= 1
        return root
