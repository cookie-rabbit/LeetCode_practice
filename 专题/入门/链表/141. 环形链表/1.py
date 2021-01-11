# https://leetcode-cn.com/problems/linked-list-cycle/
# 给定一个链表，判断链表中是否有环。
#
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，
# 我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
# 注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
#
# 如果链表中存在环，则返回 true 。 否则，返回 false 。
#
# 进阶：
#
# 你能用 O(1)（即，常量）内存解决此问题吗？
#
# 输入：head = [3,2,0,-4], pos = 1
# 输出：true
# 解释：链表中有一个环，其尾部连接到第二个节点。
#
# 输入：head = [1,2], pos = 0
# 输出：true
# 解释：链表中有一个环，其尾部连接到第一个节点。
#
# 输入：head = [1], pos = -1
# 输出：false
# 解释：链表中没有环。
from node import ListNode


class Solution:
    # 哈希表
    def hasCycle(self, head: ListNode) -> bool:
        # 1. python map
        m = {}
        while head:
            if m.get(head):
                return True
            m[head] = 1
            head = head.next
        return False

    # 快慢指针
    def hasCycle2(self, head: ListNode) -> bool:
        # 2. slow fast point
        sp, fp, si = head, head, False
        while fp:
            if si:
                sp = sp.next
                si = False
            else:
                si = True
            fp = fp.next
            if sp == fp:
                return True
        return False

    # 链表计数
    def hasCycle3(self, head: ListNode) -> bool:
        # 3. 计数 10000
        count = 0
        while head and count <= 10000:
            count, head = count + 1, head.next
        return count > 10000

    # 链表反转
    def hasCycle4(self, head: ListNode) -> bool:
        # 4. 列表倒置
        if not head or not head.next:
            return False
        p, q = None, head
        while q:
            u, p, q = p, q, q.next
            p.next = u
        return head == q

    # 标记 val 值
    def hasCycle5(self, head: ListNode) -> bool:
        # 5. 标记val
        while head:
            # s = getattr(head, 's', None)  # 获取s属性
            # if s:  # 判断s属性
            if head.val == '1':
                return True
            # head.s = 1  # 添加s属性
            head.val = '1'
            head = head.next
        return False
