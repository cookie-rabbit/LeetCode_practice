# https://leetcode-cn.com/problems/palindrome-linked-list/
# 请判断一个链表是否为回文链表。
#
# 示例 1:
#
# 输入: 1->2
# 输出: false
# 示例 2:
#
# 输入: 1->2->2->1
# 输出: true
# 进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from node import ListNode


class Solution:
    """
    有两种常用的列表实现，分别为数组列表和链表。如果我们想在列表中存储值，它们是如何实现的呢？

    数组列表底层是使用数组存储值，我们可以通过索引在 O(1)O(1) 的时间访问列表任何位置的值，这是由基于内存寻址的方式。

    链表存储的是称为节点的对象，每个节点保存一个值和指向下一个节点的指针。访问某个特定索引的节点需要 O(n)O(n) 的时间，因为要通过指针获取
    到下一个位置的节点。

    确定数组列表是否回文很简单，我们可以使用双指针法来比较两端的元素，并向中间移动。一个指针从起点向中间移动，另一个指针从终点向中间移动。
    这需要 O(n)O(n) 的时间，因为访问每个元素的时间是 O(1)O(1)，而有 nn 个元素要访问。

    然而同样的方法在链表上操作并不简单，因为不论是正向访问还是反向访问都不是 O(1)O(1)。而将链表的值复制到数组列表中是 O(n)O(n)，
    因此最简单的方法就是将链表的值复制到数组列表中，再使用双指针法判断。

    算法

    一共为两个步骤：

    1.复制链表值到数组列表中。
    2.使用双指针法判断是否为回文。

    第一步，我们需要遍历链表将值复制到数组列表中。我们用 currentNode 指向当前节点。每次迭代向数组添加 currentNode.val，
    并更新 currentNode = currentNode.next，当 currentNode = null 时停止循环。

    执行第二步的最佳方法取决于你使用的语言。在 Python 中，很容易构造一个列表的反向副本，也很容易比较两个列表。而在其他语言中，
    就没有那么简单。因此最好使用双指针法来检查是否为回文。我们在起点放置一个指针，在结尾放置一个指针，每一次迭代判断两个指针指向的元素是否相同，若不同，返回 false；相同则将两个指针向内移动，并继续判断，直到两个指针相遇。

    在编码的过程中，注意我们比较的是节点值的大小，而不是节点本身。正确的比较方式是：node_1.val == node_2.val，
    而 node_1 == node_2 是错误的。
    """

    # 方法一：将值复制到数组中后用双指针法(python 这里没用双指针)
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]

    """
    方法二：递归
    思路
    
    为了想出使用空间复杂度为 O(1)的算法，你可能想过使用递归来解决，但是这仍然需要 O(n) 的空间复杂度。
    
    递归为我们提供了一种优雅的方式来方向遍历节点。
    function print_values_in_reverse(ListNode head)
        if head is NOT null
            print_values_in_reverse(head.next)
            print head.val
    
    如果使用递归反向迭代节点，同时使用递归函数外的变量向前迭代，就可以判断链表是否为回文。
    
    算法
    currentNode 指针是先到尾节点，由于递归的特性再从后往前进行比较。frontPointer 是递归函数外的指针。
    若 currentNode.val != frontPointer.val 则返回 false。反之，frontPointer 向前移动并返回 true。
    
    算法的正确性在于递归处理节点的顺序是相反的（回顾上面打印的算法），而我们在函数外又记录了一个变量，因此从本质上，
    我们同时在正向和逆向迭代匹配。
    """

    def isPalindrome2(self, head: ListNode) -> bool:

        self.front_pointer = head

        def recursively_check(current_node=head):
            if current_node is not None:
                # 下面这个判断，只要递归过程有任何一个 False,就会一直传递到最外层并返回 False
                # 利用递归，current_node 其实是从最后一个节点的 next 也就是 None 开始的,不过会被判断条件直接跳过
                # 所以在判断条件内的第一个 current_node 就是链表的末尾节点
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                # 前面的指针向后走一位
                self.front_pointer = self.front_pointer.next
            return True

        return recursively_check()

    """
    方法三：快慢指针
    思路
    
    避免使用 O(n)额外空间的方法就是改变输入。
    
    我们可以将链表的后半部分反转（修改链表结构），然后将前半部分和后半部分进行比较。比较完成后我们应该将链表恢复原样。
    虽然不需要恢复也能通过测试用例，但是使用该函数的人通常不希望链表结构被更改。

    算法
    
    整个流程可以分为以下五个步骤：
    
    1.找到前半部分链表的尾节点。
    2.反转后半部分链表。
    3.判断是否回文。
    4.恢复链表。
    5.返回结果。
    执行步骤一，我们可以计算链表节点的数量，然后遍历链表找到前半部分的尾节点。
    
    我们也可以使用快慢指针在一次遍历中找到：慢指针一次走一步，快指针一次走两步，快慢指针同时出发。当快指针移动到链表的末尾时，
    慢指针恰好到链表的中间。通过慢指针将链表分为两部分。
    
    若链表有奇数个节点，则中间的节点应该看作是前半部分。
    
    步骤二可以使用「206. 反转链表」问题中的解决方法来反转链表的后半部分。
    
    步骤三比较两个部分的值，当后半部分到达末尾则比较完成，可以忽略计数情况中的中间节点。
    
    步骤四与步骤二使用的函数相同，再反转一次恢复链表本身。
    """

    # 快慢指针
    # 该方法虽然可以将空间复杂度降到 O(1)，但是在并发环境下，该方法也有缺点。在并发环境下，
    # 函数运行时需要锁定其他线程或进程对链表的访问，因为在函数执行过程中链表会被修改。
    def isPalindrome3(self, head: ListNode) -> bool:
        if head is None:
            return True

        # 找到前半部分链表的尾节点并反转后半部分链表
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # 判断是否回文
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # 还原链表并返回结果
        first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous
