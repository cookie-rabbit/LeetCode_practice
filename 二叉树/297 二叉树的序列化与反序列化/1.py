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

from 二叉树.tree_node import TreeNode


class Codec:

    # 序列化二叉树
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # 异常处理
        if not root:
            return "[]"

        queue = collections.deque()
        queue.append(root)
        res = []
        # 把二叉树的节点一个个弹出，加入列表中，
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                # 该节点的子节点排到队列最后
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            #  如果不存在则存入一个 'null'
            else:
                res.append("null")

        # 注意拼成字符串返回
        return '[' + ','.join(res) + ']'

    # 反序列化
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # 异常处理
        if data == '[]':
            return None

        # vals 是列表 data 从第二位开始到倒数第二位结束的截取片段，这是为了去掉字符串两边的 '[', ']'
        vals, i = data[1:-1].split(','), 1

        # 列表第一个节点即为根节点
        root = TreeNode(int(vals[0]))
        queue = collections.deque()
        queue.append(root)
        while queue:
            # 拿出队列中的第一个点
            node = queue.popleft()
            # 如 i 索引位的值不为 'null'，则先放左侧，再放右侧
            # 否则直接跳过这一位
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root
