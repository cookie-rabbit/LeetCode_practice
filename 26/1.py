class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 1
        while i <= len(nums) - 1:
            if nums[i] == nums[i - 1]:
                del nums[i]
            else:
                i += 1
        return len(nums)


s = Solution().removeDuplicates([1,1,2,2,3])
print(s)
