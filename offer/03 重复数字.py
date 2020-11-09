"""
找出数组中重复的数字。

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：
输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3
 
限制：
2 <= n <= 100000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof
"""


class Solution(object):

    def findRepeatNumber_1(self, nums):
        """方法1，元素数过去"""

        for i in nums:
            tar = i
            num = 0
            for j in nums:
                if j == tar:
                    num += 1
            if num > 1:
                return i

    def findRepeatNumber_2(self, nums):
        """方法2，将列表转为集合，两者相减，如还存在则说明重复"""
        if len(nums) == len(set(nums)):
            return None
        a = set(nums)
        for i in a:
            if i in nums:
                nums.remove(i)
            if i in nums:
                print(i)

    """上面两种方法速度太慢，超时"""

    def findRepeatNumber_3(self, nums):
        """方法3，删除法，不重复元素，删除完后检测是否有剩余元素
        勉强通过，10%用时，6%内存
        和方法2思想一致，只是不用in方法，节约了时间
        """
        if len(nums) == len(set(nums)):
            return None
        a = set(nums)
        for i in a:
            nums.remove(i)
        return nums[0]

    def findRepeatNumber_4(self, nums):
        """方法4，将列表排序，查看相邻元素是否有重复的
        通过，68%用时，6%内存
        """
        if len(nums) == len(set(nums)):
            return None
        nums.sort()
        begin = 0
        while nums[begin] != nums[begin + 1]:
            begin += 1
        else:
            print(nums[begin])

    def findRepeatNumber_5(self, nums):
        """方法5，
        用时94%，内存41%
        哈希表，利用哈希表查询速度快的特性，当一个元素已经存在于表中则将其输出出来"""
        ss = dict()
        for i in nums:
            if i in ss:
                return i
            else:
                ss[i] = 1
        return None

        """用下面这个集合法也可以"""
        ss = set()
        for i in nums:
            if i in ss:
                return i
            else:
                ss.add(i)
        return None

    def findRepeatNumber_6(self, nums):
        """
        方法6
        用时94%，内存83%
        题目中有‘在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内’这一条件，因此
        可以将 nums 里的数字均放入一个长度为 n ，键为从 0~n-1 的字典内，
        `索引和值存在一对多的映射关系
        `如果val值与其对应的索引idx相同，则说明无需交换，直接跳过
        `否则，如果val值与val值对应索引处的值相等，则说明val重复，否则交换值
        `其实可以理解为查找某处索引对应多个相同值的case
        """
        for index, value in enumerate(nums):
            while index != value:
                if value == nums[value]:
                    return value
                # 这里的交换，是指将 nums[index] 的值，放到 nums[value] 中，也就是值和索引对应，至于从 nums[value] 交换过来的值
                # 则无所谓。
                nums[index], nums[value] = nums[value], nums[index]
        return None
