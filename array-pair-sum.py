class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        s = 0
        i = 0
        while i < len(nums)-1:
            s += min(nums[i], nums[i+1])
            i += 2
        return s