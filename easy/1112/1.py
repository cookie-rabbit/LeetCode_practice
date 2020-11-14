# 给你两个数组，arr1 和 arr2，
# arr2 中的元素各不相同
# arr2 中的每个元素都出现在 arr1 中
# 对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。
# https://leetcode-cn.com/problems/relative-sort-array/


from copy import deepcopy
from typing import List

arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ss = []
        arr3 = deepcopy(arr1)

        for j in arr2:
            for i in arr1:
                if i == j:
                    ss.append(i)
                    arr3.remove(i)
        ss.extend(sorted(arr3))
        return ss


a = Solution().relativeSortArray(arr1, arr2)
print(a)
