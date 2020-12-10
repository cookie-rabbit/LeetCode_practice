# https://leetcode-cn.com/problems/design-circular-queue/
# 设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。
# 它也被称为“环形缓冲器”。
#
# 循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，
# 即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存储新的值。
#
# 你的实现应该支持如下操作：
#
# MyCircularQueue(k): 构造器，设置队列长度为 k 。
# Front: 从队首获取元素。如果队列为空，返回 -1 。
# Rear: 获取队尾元素。如果队列为空，返回 -1 。
# enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
# deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
# isEmpty(): 检查循环队列是否为空。
# isFull(): 检查循环队列是否已满。
#
#
# 示例：
#
# MyCircularQueue circularQueue = new MyCircularQueue(3); // 设置长度为 3
# circularQueue.enQueue(1); // 返回 true
# circularQueue.enQueue(2); // 返回 true
# circularQueue.enQueue(3); // 返回 true
# circularQueue.enQueue(4); // 返回 false，队列已满
# circularQueue.Rear(); // 返回 3
# circularQueue.isFull(); // 返回 true
# circularQueue.deQueue(); // 返回 true
# circularQueue.enQueue(4); // 返回 true
# circularQueue.Rear(); // 返回 4
#
#
# 提示：
#
# 所有的值都在 0 至 1000 的范围内；
# 操作数将在 1 至 1000 的范围内；
# 请不要使用内置的队列库。

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        # queue：一个固定大小的数组，用于保存循环队列的元素。
        #
        # headIndex：一个整数，保存队首 head 的索引。
        #
        # count：循环队列当前的长度，即循环队列中的元素数量。使用 hadIndex 和 count 可以计算出队尾元素的索引，因此不需要队尾属性。
        #
        # capacity：循环队列的容量，即队列中最多可以容纳的元素数量。该属性不是必需的，因为队列容量可以通过数组属性得到，
        # 但是由于该属性经常使用，所以我们选择保留它。这样可以不用在 Python 中每次调用 len(queue) 中获取容量。
        # 但是在 Java 中通过 queue.length 获取容量更加高效。为了保持一致性，在两种方案中都保留该属性。
        self.queue = [0] * k
        self.headIndex = 0
        self.count = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.count == self.capacity:
            return False
        self.queue[(self.headIndex + self.count) % self.capacity] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.count == 0:
            return False
        self.headIndex = (self.headIndex + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.count == 0:
            return -1
        return self.queue[self.headIndex]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        # empty queue
        if self.count == 0:
            return -1
        return self.queue[(self.headIndex + self.count - 1) % self.capacity]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.count == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.count == self.capacity
