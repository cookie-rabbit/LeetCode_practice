def recursive(n: list, m: int, stack: list) -> None:
    if m == 0:
        print(stack)
        return
    """递归，找出 m 与数组前 i+1 个值的差，如果差为0，说明恰好是一个符合条件的数组，将其输出"""
    for i in range(0, len(n)):
        # 注意，因为我们的数组中可能存在负数，因此下面这个判断条件使用条件是对原数组必须进行排序，否则会有遗漏
        if n[i] <= m:
            stack.append(n[i])
            recursive(n[i + 1:], m - n[i], stack)
            stack.pop()
        else:
            break
        # 如果不排序，则不进行if判断，直接用递归语句
        # stack.append(n[i])
        # recursive(n[i + 1:], m - n[i], stack)
        # stack.pop()


# 输入数组，用空格分开，支持负数
int_list = input()
# 输入目标值
target = int(input())

# 如果需要输出结果按数字大小排序则加 sorted，否则不加
int_list = sorted([int(i) for i in int_list.split()])
# int_list = [int(i) for i in int_list.split()]

recursive(int_list, target, [])
