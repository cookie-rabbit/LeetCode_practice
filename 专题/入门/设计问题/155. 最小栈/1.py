# https://leetcode-cn.com/problems/min-stack/
# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
#
# push(x) —— 将元素 x 推入栈中。
# pop() —— 删除栈顶的元素。
# top() —— 获取栈顶元素。
# getMin() —— 检索栈中的最小元素。
#  
#
# 示例:
#
# 输入：
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
#
# 输出：
# [null,null,null,null,-3,null,0,-2]
#
# 解释：
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.
#  
#
# 提示：
#
# pop、top 和 getMin 操作总是在 非空栈 上调用。
import copy


class MinStack(object):
    # 题目要求在常数时间内获得栈中的最小值，因此不能在 getMin() 的时候再去计算最小值，最好应该在 push 或者 pop 的时候就
    # 已经计算好了当前栈中的最小值。
    #
    # 前排的众多题解中，基本都讲了「辅助栈」的概念，这是一种常见的思路，但是有没有更容易懂的方法呢？
    #
    # 可以用一个栈，这个栈同时保存的是每个数字 x 进栈的时候的值与插入该值后的栈内最小值。即每次新元素 x 入栈的时候保存一个元组：
    # （当前值 x，栈内最小值）。
    #
    # 这个元组是一个整体，同时进栈和出栈。即栈顶同时有值和栈内最小值，top()
    # 函数是获取栈顶的当前值，即栈顶元组的第一个值； getMin()
    # 函数是获取栈内最小值，即栈顶元组的第二个值；pop()
    # 函数时删除栈顶的元组。
    #
    # 每次新元素入栈时，要求新的栈内最小值：比较当前新插入元素 x 和当前栈内最小值（即栈顶元组的第二个值）的大小。
    #
    # 新元素入栈：当栈为空，保存元组(x, x)；当栈不空，保存元组(x, min(此前栈内最小值， x)))
    # 出栈：删除栈顶的元组。

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.stack.append((x, x))
        else:
            self.stack.append((x, min(x, self.stack[-1][1])))

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]


class MinStack:
    # 解题思路：
    # 借用一个辅助栈min_stack，用于存获取stack中最小值。
    #
    # 算法流程：
    # push() 方法：每当 push() 新值进来时，如果小于等于 min_stack 栈顶值，则一起push() 到 min_stack，即更新了栈顶最小值；
    # pop() 方法：判断将 pop() 出去的元素值是否是 min_stack 栈顶元素值（即最小值），如果是则将 min_stack 栈顶元素一起 pop()，
    # 这样可以保证 min_stack 栈顶元素始终是 stack 中的最小值。
    # getMin() 方法：返回min_stack栈顶即可。
    # min_stack 作用分析 min_stack 等价于遍历 stack 所有元素，把升序的数字都删除掉，留下一个从栈底到栈顶降序的栈。
    # 相当于给 stack 中的降序元素做了标记，每当 pop() 这些降序元素，min_stack 会将相应的栈顶元素 pop() 出去，
    # 保证其栈顶元素始终是 stack 中的最小元素。
    #
    # 复杂度分析：
    # 时间复杂度 O(1)：压栈，出栈，获取最小值的时间复杂度都为 O(1)。
    # 空间复杂度 O(N)：包含 N 个元素辅助栈占用线性大小的额外空间。

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
