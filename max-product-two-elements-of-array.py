class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currHigh = 0
        nums.sort()
        return (nums[-1]-1)*(nums[-2]-1)