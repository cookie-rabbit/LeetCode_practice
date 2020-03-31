class Solution:
    def searchInsert(self, nums, target) -> int:
        ss = len(nums)
        for i in range(ss):
            if target == nums[i]:
                return i
            if target < nums[i]:
                return i
            if target > nums[-1]:
                return ss


a = Solution().searchInsert([1, 3, 5, 6], 4)
print(a)
