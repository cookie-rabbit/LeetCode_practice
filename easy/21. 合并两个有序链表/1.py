# https://leetcode-cn.com/problems/merge-two-sorted-lists/
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
# 示例 2：
#
# 输入：l1 = [], l2 = []
# 输出：[]
# 示例 3：
#
# 输入：l1 = [], l2 = [0]
# 输出：[0]
# 提示：
#
# 两个链表的节点数目范围是 [0, 50]
# -100 <= Node.val <= 100
# l1 和 l2 均按 非递减顺序 排列

class Solution:
    # 递归法
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
