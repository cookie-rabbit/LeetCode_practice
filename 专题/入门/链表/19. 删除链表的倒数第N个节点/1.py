# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例：
#
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
#
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 说明：
#
# 给定的 n 保证是有效的。
#
# 进阶：
#
# 你能尝试使用一趟扫描实现吗？

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from node import ListNode


class Solution:
    # 循环迭代，强行查找
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # dummy,添加头节点
        dummy = ListNode(0)
        dummy.next = head

        # 获取链表长度
        cur, lenth = head, 0
        while cur:
            lenth += 1
            cur = cur.next

        # 找到倒数第 n 个节点前的那个节点
        cur = dummy
        # 以示例为例，注意长度是 5 而不是 4
        for _ in range(lenth - n):
            cur = cur.next

        # 删除节点并重新链接
        cur.next = cur.next.next
        return dummy.next

    # 快慢指针法
    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        # dummy,添加头节点
        dummy = ListNode(0)
        dummy.next = head

        # 快指针先走 n 步
        slow, fast = dummy, dummy
        for _ in range(n):
            fast = fast.next

        # 快慢指针同时走，直到 fast 指针达到链表尾部节点，此时 slow 到达倒数第 n 个节点的前一个节点
        while fast and fast.next:
            slow, fast = slow.next, fast.next

        # 删除节点并重新链接
        slow.next = slow.next.next
        return dummy.next

    # 递归迭代 回溯时，进行迭代计数
    def removeNthFromEnd3(self, head: ListNode, n: int) -> ListNode:
        if not head:
            self.count = 0
            return head
        head.next = self.removeNthFromEnd3(head.next, n)
        self.count += 1
        return head.next if self.count == n else head
