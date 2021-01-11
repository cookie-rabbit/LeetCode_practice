# https://leetcode-cn.com/problems/reverse-linked-list/
# 反转一个单链表。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
from node import ListNode


class Solution:

    # 迭代法
    def reverseList(self, head: ListNode) -> ListNode:
        # 注意需要 pre 用来存储当前节点，否则 cur 一旦指向下一个节点，前面的数据就找不到了
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

    # 递归停止条件：当前节点为空或者只剩当前一个节点
    # 假设当前链表为：1 -> 2 -> 3 -> 4 -> 5，当前 head 为 1
    # 调用递归函数后，返回 1 -> 2 <- 3 <- 4 <- 5，newhead 为 5
    # head.next.next = head 实现从 1 -> 2 到 1 <- 2
    # head.next = None 实现链表尾部指向空

    # 始终注意，链表是一个整体，当重新指定链表头后，给链表头的 next 指定值就是在延长该链表
    def reverseList2(self, head: ListNode) -> ListNode:
        if not head or head.next == None:
            return head
        res = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        return res
