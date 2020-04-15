class Solution(object):
    def isValid(self, s):

        # stack用于跟踪开括号。
        stack = []

        # Hash map 用于记录映射关系，方便添加其他对应。
        mapping = {")": "(", "}": "{", "]": "["}

        # 对于给定字符串中的每一个括号
        for char in s:

            # 如果该括号是一个闭括号
            if char in mapping:

                # 弹出stack中的顶层元素，如果stack为空则记录为虚拟值'#'
                top_element = stack.pop() if stack else '#'

                # 根据映射关系，比较哈希映射值与弹出元素，如果不相符则直接返回无效
                # 这种情况下，说明该闭括号对应的开括号与最近压入栈中的开括号不同
                # 说明两个相邻的开闭括号不匹配，则直接返回无效
                if mapping[char] != top_element:
                    return False
            else:
                # 将开括号压入栈中
                stack.append(char)

        # 最终如果栈中为空，说明传入字符串有效，否则无效；
        return not stack
