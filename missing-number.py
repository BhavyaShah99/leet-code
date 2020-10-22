class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[len(nums)-1] != len(nums):
            return len(nums)
        else:
            for i in range(0,len(nums)):
                if nums[i] != i:
                    return i
        return 0