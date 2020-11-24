# https://leetcode-cn.com/problems/insertion-sort-list/
# 对链表进行插入排序。
# 插入排序算法：
#
# 插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
# 每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
# 重复直到所有输入数据插入完为止。
#
# 示例 1：
#
# 输入: 4->2->1->3
# 输出: 1->2->3->4
# 示例2：
#
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5

# 定义一个单链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 4->2->1->3
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # 设置虚拟头结点
        dummy = ListNode(0)
        # cur 指向链表的第一个真实节点
        cur = head
        while cur:
            pre = dummy
            # pre.next.val 比 当前节点值小时继续前进
            while pre.next and pre.next.val <= cur.val:
                pre = pre.next
            #
            tmp = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = tmp
        return dummy.next
