"""给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。"""


# 定义一个单链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# val代表值，next代表指针


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        # head是一个链表，并在后续的判断中会不断改变。
        dummyHead, dummyHead.next = ListNode(0), head
        while head is not None and head.next is not None:
            # 判断当前指针和指针下一位的值是否相等，相等时跳过下一位，指针下一位替换为下两位，如此反复。
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                # 不相等时指针指向下一位，从下一位继续该逻辑循环。
                head = head.next
        #     在整个过程中，
        return dummyHead.next
