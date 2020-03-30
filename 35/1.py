class Solution:
    def searchInsert(self, nums, target) -> int:
        a = str(nums).find(str(target))
        if a == -1:
            a = 4
        return a


a = Solution().searchInsert([1, 3, 5, 6], 4)
print(a)
