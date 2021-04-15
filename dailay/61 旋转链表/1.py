# https://leetcode-cn.com/problems/rotate-list/
# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置，求新链表。
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[4,5,1,2,3]
#
# 输入：head = [0,1,2], k = 4
# 输出：[2,0,1]
#
# 提示：
# 链表中节点的数目在范围 [0, 500] 内
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109

class Solution:
    # 向后走了 k 位，则新链表的头一定是 -k，简单的想就是 -k + k = 0，说明 -k 就是新链表的头，当然，k要取模，也就是去除多余的循环。
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head
        # 求链表长度
        _len = 0
        cur = head
        while cur:
            _len += 1
            cur = cur.next
        # 对长度取模
        k %= _len
        if k == 0:
            return head
        # 让 fast 先向后走 k 步
        fast, slow = head, head
        while k:
            fast = fast.next
            k -= 1
        # 此时 slow 和 fast 之间的距离是 k；fast 指向第 k+1 个节点
        # 当 fast.next 为空时，fast 指向链表最后一个节点，slow 指向倒数第 k + 1 个节点

        # 上面这么做的目的是找出 -k，方法是先拉开 k 的距离，然后当 fast 指向最后一位时，slow 因为距离 fast 的距离为 k，
        # 所以 slow 指向 k+1，则 slow.next 指向的就是 -k，也就是新链表的头
        while fast.next:
            fast = fast.next
            slow = slow.next
        # newHead 是倒数第 k 个节点，即新链表的头
        # 倒数第 k 个节点一定是新链表的头,fast 是用来定位新链表头的
        # 因为 fast 走到底时，slow 的 next 一定是第 k 个节点。
        newHead = slow.next
        # 让倒数第 k + 1 个节点 和 倒数第 k 个节点断开
        slow.next = None
        # 让最后一个节点指向原始链表的头
        fast.next = head
        return newHead
